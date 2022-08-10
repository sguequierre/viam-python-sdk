from dataclasses import dataclass
from multiprocessing import Queue
from random import random
from secrets import choice
from typing import Any, Dict, List, Optional, Tuple

from PIL import Image
from viam.components.arm import Arm, JointPositions
from viam.components.base import Base
from viam.components.board import Board
from viam.components.board.board import PostProcessor
from viam.components.camera import Camera, IntrinsicParameters
from viam.components.gantry import Gantry
from viam.components.generic import Generic as GenericComponent
from viam.components.gps import GPS
from viam.components.gripper import Gripper
from viam.components.imu import IMU, Acceleration, AngularVelocity, EulerAngles, Magnetometer, Orientation
from viam.components.input import Control, ControlFunction, Controller, Event, EventType
from viam.components.motor import Motor
from viam.components.pose_tracker import PoseTracker
from viam.components.sensor import Sensor
from viam.components.servo import Servo
from viam.components.types import CameraMimeType
from viam.errors import ComponentNotFoundError
from viam.proto.api.common import AnalogStatus, BoardStatus, DigitalInterruptStatus, Pose, PoseInFrame, Vector3, WorldState


class MockArm(Arm):
    def __init__(self, name: str):
        self.position = Pose(
            x=1,
            y=2,
            z=3,
            o_x=2,
            o_y=3,
            o_z=4,
            theta=20,
        )
        self.joint_positions = JointPositions(values=[0, 0, 0, 0, 0, 0])
        self.is_stopped = True
        self.extra = None
        super().__init__(name)

    async def get_end_position(self, extra: Optional[Dict[str, Any]] = None) -> Pose:
        self.extra = extra
        return self.position

    async def move_to_position(self, pose: Pose, world_state: Optional[WorldState] = None, extra: Optional[Dict[str, Any]] = None):
        self.position = pose
        self.is_stopped = False
        self.extra = extra

    async def get_joint_positions(self, extra: Optional[Dict[str, Any]] = None) -> JointPositions:
        self.extra = extra
        return self.joint_positions

    async def move_to_joint_positions(self, positions: JointPositions, extra: Optional[Dict[str, Any]] = None):
        self.joint_positions = positions
        self.is_stopped = False
        self.extra = extra

    async def stop(self, extra: Optional[Dict[str, Any]] = None):
        self.is_stopped = True
        self.extra = extra

    async def is_moving(self) -> bool:
        return not self.is_stopped


class MockBase(Base):
    def __init__(self, name: str):
        self.position = 0
        self.angle = 0
        self.stopped = True
        self.linear_pwr = Vector3(x=0, y=0, z=0)
        self.angular_pwr = Vector3(x=0, y=0, z=0)
        self.linear_vel = Vector3(x=0, y=0, z=0)
        self.angular_vel = Vector3(x=0, y=0, z=0)
        self.extra: Optional[Dict[str, Any]] = None
        super().__init__(name)

    async def move_straight(self, distance: int, velocity: float, extra: Optional[Dict[str, Any]] = None):
        if distance == 0 or velocity == 0:
            return await self.stop()

        if velocity > 0:
            self.position += distance
        else:
            self.position -= distance

        self.stopped = False
        self.extra = extra

    async def move_arc(
        self,
        distance: int,
        velocity: float,
        angle: float,
        extra: Optional[Dict[str, Any]] = None,
    ):
        if distance == 0:
            return await self.spin(angle, velocity)

        if velocity == 0:
            return await self.stop()

        if velocity > 0:
            self.position += distance
            self.angle += angle
        else:
            self.position -= distance
            self.angle -= angle

        self.stopped = False
        self.extra = extra

    async def spin(self, angle: float, velocity: float, extra: Optional[Dict[str, Any]] = None):
        if angle == 0 or velocity == 0:
            return await self.stop()

        if velocity > 0:
            self.angle += angle
        else:
            self.angle -= angle

        self.stopped = False
        self.extra = extra

    async def set_velocity(self, linear: Vector3, angular: Vector3, extra: Optional[Dict[str, Any]] = None):
        self.linear_vel = linear
        self.angular_vel = angular
        self.extra = extra

    async def set_power(self, linear: Vector3, angular: Vector3, extra: Optional[Dict[str, Any]] = None):
        self.linear_pwr = linear
        self.angular_pwr = angular
        self.extra = extra

    async def stop(self, extra: Optional[Dict[str, Any]] = None):
        self.stopped = True
        self.extra = extra

    async def is_moving(self) -> bool:
        return not self.stopped


class MockAnalogReader(Board.AnalogReader):
    def __init__(self, name: str, value: int):
        self.value = value
        super().__init__(name)

    async def read(self, extra: Optional[Dict[str, Any]] = None) -> int:
        self.extra = extra
        return self.value


class MockDigitalInterrupt(Board.DigitalInterrupt):
    def __init__(self, name: str):
        self.high = False
        self.last_tick = 0
        self.num_ticks = 0
        self.callbacks: List[Queue] = []
        self.post_processors: List[PostProcessor] = []
        super().__init__(name)

    async def value(self, extra: Optional[Dict[str, Any]] = None) -> int:
        self.extra = extra
        return self.num_ticks

    async def tick(self, high: bool, nanos: int):
        self.high = high
        self.last_tick = nanos
        self.num_ticks += 1

    async def add_callback(self, queue: Queue):
        self.callbacks.append(queue)

    async def add_post_processor(self, processor: PostProcessor):
        self.post_processors.append(processor)


class MockGPIOPin(Board.GPIOPin):
    def __init__(self, name: str):
        self.high = False
        self.pwm = 0.0
        self.pwm_freq = 0
        super().__init__(name)

    async def get(self, extra: Optional[Dict[str, Any]] = None) -> bool:
        self.extra = extra
        return self.high

    async def set(self, high: bool, extra: Optional[Dict[str, Any]] = None):
        self.high = high
        self.extra = extra

    async def get_pwm(self, extra: Optional[Dict[str, Any]] = None) -> float:
        self.extra = extra
        return self.pwm

    async def set_pwm(self, duty_cycle: float, extra: Optional[Dict[str, Any]] = None):
        self.pwm = duty_cycle
        self.extra = extra

    async def get_pwm_frequency(self, extra: Optional[Dict[str, Any]] = None) -> int:
        self.extra = extra
        return self.pwm_freq

    async def set_pwm_frequency(self, frequency: int, extra: Optional[Dict[str, Any]] = None):
        self.pwm_freq = frequency
        self.extra = extra


class MockBoard(Board):
    def __init__(
        self,
        name: str,
        analog_readers: Dict[str, Board.AnalogReader],
        digital_interrupts: Dict[str, Board.DigitalInterrupt],
        gpio_pins: Dict[str, Board.GPIOPin],
    ):
        self.analog_readers = analog_readers
        self.digital_interrupts = digital_interrupts
        self.gpios = gpio_pins
        super().__init__(name)

    async def analog_reader_by_name(self, name: str) -> Board.AnalogReader:
        try:
            return self.analog_readers[name]
        except KeyError:
            raise ComponentNotFoundError("Board.AnalogReader", name)

    async def digital_interrupt_by_name(self, name: str) -> Board.DigitalInterrupt:
        try:
            return self.digital_interrupts[name]
        except KeyError:
            raise ComponentNotFoundError("Board.DigitalInterrupt", name)

    async def gpio_pin_by_name(self, name: str) -> Board.GPIOPin:
        try:
            return self.gpios[name]
        except KeyError:
            raise ComponentNotFoundError("Board.GPIOPin", name)

    async def analog_reader_names(self) -> List[str]:
        return [key for key in self.analog_readers.keys()]

    async def digital_interrupt_names(self) -> List[str]:
        return [key for key in self.digital_interrupts.keys()]

    async def status(self, extra: Optional[Dict[str, Any]] = None) -> BoardStatus:
        self.extra = extra
        return BoardStatus(
            analogs={name: AnalogStatus(value=await analog.read()) for (name, analog) in self.analog_readers.items()},
            digital_interrupts={name: DigitalInterruptStatus(value=await di.value()) for (name, di) in self.digital_interrupts.items()},
        )

    async def model_attributes(self) -> Board.Attributes:
        return Board.Attributes(remote=True)


class MockCamera(Camera):
    def __init__(self, name: str):
        self.image = Image.new("RGBA", (100, 100), "#AABBCCDD")
        self.point_cloud = b"THIS IS A POINT CLOUD"
        self.props = IntrinsicParameters(width_px=1, height_px=2, focal_x_px=3, focal_y_px=4, center_x_px=5, center_y_px=6)
        super().__init__(name)

    async def get_frame(self) -> Image.Image:
        return self.image

    async def get_point_cloud(self) -> Tuple[bytes, str]:
        return self.point_cloud, CameraMimeType.PCD.value

    async def get_properties(self) -> IntrinsicParameters:
        return self.props


class MockGantry(Gantry):
    def __init__(self, name: str, position: List[float], lengths: List[float]):
        self.position = position
        self.lengths = lengths
        self.is_stopped = True
        self.extra = None
        super().__init__(name)

    async def get_position(self, extra: Optional[Dict[str, Any]] = None) -> List[float]:
        self.extra = extra
        return self.position

    async def move_to_position(
        self,
        positions: List[float],
        world_state: Optional[WorldState] = None,
        extra: Optional[Dict[str, Any]] = None,
    ):
        self.position = positions
        self.is_stopped = False
        self.extra = extra

    async def get_lengths(self, extra: Optional[Dict[str, Any]] = None) -> List[float]:
        self.extra = extra
        return self.lengths

    async def stop(self, extra: Optional[Dict[str, Any]] = None):
        self.extra = extra
        self.is_stopped = True

    async def is_moving(self) -> bool:
        return not self.is_stopped


class MockGeneric(GenericComponent):
    async def do(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return {key: True for key in command.keys()}


class MockGPS(GPS):
    def __init__(self, name: str, location: GPS.Point, altitude: float, speed: float):
        self.location = location
        self.altitude = altitude
        self.speed = speed
        super().__init__(name)

    async def read_location(self) -> GPS.Point:
        return self.location

    async def read_altitude(self) -> float:
        return self.altitude

    async def read_speed(self) -> float:
        return self.speed


class MockGripper(Gripper):
    def __init__(self, name: str):
        self.opened = False
        self.is_stopped = True
        super().__init__(name)

    async def open(self):
        self.opened = True
        self.is_stopped = False

    async def grab(self) -> bool:
        self.opened = False
        self.is_stopped = False
        return choice([True, False])

    async def stop(self):
        self.is_stopped = True

    async def is_moving(self) -> bool:
        return not self.is_stopped


class MockIMU(IMU):
    @dataclass
    class Result:
        acceleration: Acceleration
        angular_velocity: AngularVelocity
        orentation: Orientation
        magnetometer: Magnetometer

    def __init__(
        self,
        name: str,
        result: Result = Result(
            Acceleration(x_mm_per_sec_per_sec=random(), y_mm_per_sec_per_sec=random(), z_mm_per_sec_per_sec=random()),
            AngularVelocity(x_degs_per_sec=random(), y_degs_per_sec=random(), z_degs_per_sec=random()),
            Orientation(euler_angles=EulerAngles(roll_deg=random(), pitch_deg=random(), yaw_deg=random())),
            Magnetometer(x_gauss=random(), y_gauss=random(), z_gauss=random()),
        ),
    ):
        self.acceleration = result.acceleration
        self.angular_velocity = result.angular_velocity
        self.orientation = result.orentation
        self.magnetometer = result.magnetometer
        super().__init__(name)

    async def read_acceleration(self) -> Acceleration:
        return self.acceleration

    async def read_angular_velocity(self) -> AngularVelocity:
        return self.angular_velocity

    async def read_orientation(self) -> Orientation:
        return self.orientation

    async def read_magnetometer(self) -> Magnetometer:
        return self.magnetometer


class MockInputController(Controller):
    def __init__(self, name: str):
        super().__init__(name)
        self.events: Dict[Control, Event] = {}
        self.callbacks: Dict[Control, Dict[EventType, Optional[ControlFunction]]] = {}

    async def get_controls(self) -> List[Control]:
        return [
            Control.ABSOLUTE_X,
            Control.ABSOLUTE_Y,
            Control.ABSOLUTE_Z,
            Control.ABSOLUTE_RX,
            Control.ABSOLUTE_RY,
            Control.ABSOLUTE_RZ,
            Control.ABSOLUTE_HAT0_X,
            Control.ABSOLUTE_HAT0_Y,
            Control.BUTTON_SOUTH,
            Control.BUTTON_EAST,
            Control.BUTTON_WEST,
            Control.BUTTON_NORTH,
            Control.BUTTON_LT,
            Control.BUTTON_RT,
            Control.BUTTON_L_THUMB,
            Control.BUTTON_R_THUMB,
            Control.BUTTON_SELECT,
            Control.BUTTON_START,
            Control.BUTTON_MENU,
            Control.BUTTON_RECORD,
            Control.BUTTON_E_STOP,
        ]

    async def get_events(self) -> Dict[Control, Event]:
        return self.events

    def register_control_callback(self, control: Control, triggers: List[EventType], function: Optional[ControlFunction]):
        self.callbacks[control] = {trigger: function for trigger in triggers}

    async def trigger_event(self, event: Event):
        self.events[event.control] = event
        callback = self.callbacks.get(event.control, {}).get(event.event)
        if callback:
            callback(event)


class MockMotor(Motor):
    def __init__(self, name: str):
        self.position: float = 0
        self.power = 0
        self.powered = False
        self.extra = None
        super().__init__(name)

    async def set_power(self, power: float, extra: Optional[Dict[str, Any]] = None):
        self.power = power
        self.powered = power != 0
        self.extra = extra

    async def go_for(self, rpm: float, revolutions: float, extra: Optional[Dict[str, Any]] = None):
        if rpm > 0:
            self.position += revolutions
        if rpm < 0:
            self.position -= revolutions
        self.powered = False
        self.extra = extra

    async def go_to(self, rpm: float, position_revolutions: float, extra: Optional[Dict[str, Any]] = None):
        if rpm != 0:
            self.position = position_revolutions
        self.powered = False
        self.extra = extra

    async def reset_zero_position(self, offset: float, extra: Optional[Dict[str, Any]] = None):
        self.offset = offset
        self.powered = False
        self.extra = extra

    async def get_position(self, extra: Optional[Dict[str, Any]] = None) -> float:
        self.extra = extra
        return self.position

    async def get_features(self, extra: Optional[Dict[str, Any]] = None) -> Motor.Features:
        self.extra = extra
        return Motor.Features(position_reporting=True)

    async def stop(self, extra: Optional[Dict[str, Any]] = None):
        await self.set_power(0)
        self.extra = extra

    async def is_powered(self, extra: Optional[Dict[str, Any]] = None) -> bool:
        self.extra = extra
        return self.powered

    async def is_moving(self) -> bool:
        return self.powered


@dataclass
class MockPose:
    X: float
    Y: float
    Z: float
    o_X: float
    o_Y: float
    o_Z: float
    theta: float

    def to_pose_in_frame(self, frame_name: str):
        pose = Pose(x=self.X, y=self.Y, z=self.Z, o_x=self.o_X, o_y=self.o_Y, o_z=self.o_Z, theta=self.theta)
        return PoseInFrame(reference_frame=frame_name, pose=pose)


class MockPoseTracker(PoseTracker):
    def __init__(self, name: str, poses: List[MockPose]):
        pose_map: Dict[str, MockPose] = {}
        for idx, pose in enumerate(poses):
            pose_map[str(idx)] = pose
        self.poses_result = pose_map
        self.name = name

    async def get_poses(self, body_names: List[str]) -> Dict[str, PoseInFrame]:
        result: Dict[str, PoseInFrame] = {}
        for name, pose in self.poses_result.items():
            result[name] = pose.to_pose_in_frame(name)
        return result


class MockSensor(Sensor):
    def __init__(self, name: str, result: List[Any] = [0, {"foo": "bar"}, [1, 8, 2], "Hello world!"]):
        self.readings = result
        super().__init__(name)

    async def get_readings(self) -> List[Any]:
        return self.readings


class MockServo(Servo):
    def __init__(self, name: str):
        self.angle = 0
        self.is_stopped = True
        super().__init__(name)

    async def move(self, angle: int):
        self.angle = angle
        self.is_stopped = False

    async def get_position(self) -> int:
        return self.angle

    async def stop(self):
        self.is_stopped = True

    async def is_moving(self) -> bool:
        return not self.is_stopped
