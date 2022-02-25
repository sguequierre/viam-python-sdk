"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
from ..... import proto
import typing
import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class _NavigationServiceMode:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _NavigationServiceModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_NavigationServiceMode.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    NAVIGATION_SERVICE_MODE_UNSPECIFIED: NavigationServiceMode.ValueType = ...
    NAVIGATION_SERVICE_MODE_MANUAL: NavigationServiceMode.ValueType = ...
    NAVIGATION_SERVICE_MODE_WAYPOINT: NavigationServiceMode.ValueType = ...

class NavigationServiceMode(_NavigationServiceMode, metaclass=_NavigationServiceModeEnumTypeWrapper):
    pass
NAVIGATION_SERVICE_MODE_UNSPECIFIED: NavigationServiceMode.ValueType = ...
NAVIGATION_SERVICE_MODE_MANUAL: NavigationServiceMode.ValueType = ...
NAVIGATION_SERVICE_MODE_WAYPOINT: NavigationServiceMode.ValueType = ...
global___NavigationServiceMode = NavigationServiceMode

class StatusRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self) -> None:
        ...
global___StatusRequest = StatusRequest

class StatusStreamRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    EVERY_FIELD_NUMBER: builtins.int

    @property
    def every(self) -> google.protobuf.duration_pb2.Duration:
        """how often to send a new status."""
        pass

    def __init__(self, *, every: typing.Optional[google.protobuf.duration_pb2.Duration]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['every', b'every']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['every', b'every']) -> None:
        ...
global___StatusStreamRequest = StatusStreamRequest

class StatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    STATUS_FIELD_NUMBER: builtins.int

    @property
    def status(self) -> global___Status:
        ...

    def __init__(self, *, status: typing.Optional[global___Status]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['status', b'status']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['status', b'status']) -> None:
        ...
global___StatusResponse = StatusResponse

class StatusStreamResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    STATUS_FIELD_NUMBER: builtins.int

    @property
    def status(self) -> global___Status:
        ...

    def __init__(self, *, status: typing.Optional[global___Status]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['status', b'status']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['status', b'status']) -> None:
        ...
global___StatusStreamResponse = StatusStreamResponse

class Status(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    class ArmsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...

        @property
        def value(self) -> global___ArmStatus:
            ...

        def __init__(self, *, key: typing.Text=..., value: typing.Optional[global___ArmStatus]=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...

    class BasesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: builtins.bool = ...

        def __init__(self, *, key: typing.Text=..., value: builtins.bool=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...

    class GrippersEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: builtins.bool = ...

        def __init__(self, *, key: typing.Text=..., value: builtins.bool=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...

    class BoardsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...

        @property
        def value(self) -> proto.api.common.v1.common_pb2.BoardStatus:
            ...

        def __init__(self, *, key: typing.Text=..., value: typing.Optional[proto.api.common.v1.common_pb2.BoardStatus]=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...

    class CamerasEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: builtins.bool = ...

        def __init__(self, *, key: typing.Text=..., value: builtins.bool=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...

    class SensorsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...

        @property
        def value(self) -> global___SensorStatus:
            ...

        def __init__(self, *, key: typing.Text=..., value: typing.Optional[global___SensorStatus]=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...

    class FunctionsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: builtins.bool = ...

        def __init__(self, *, key: typing.Text=..., value: builtins.bool=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...

    class ServosEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...

        @property
        def value(self) -> global___ServoStatus:
            ...

        def __init__(self, *, key: typing.Text=..., value: typing.Optional[global___ServoStatus]=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...

    class MotorsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...

        @property
        def value(self) -> global___MotorStatus:
            ...

        def __init__(self, *, key: typing.Text=..., value: typing.Optional[global___MotorStatus]=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...

    class ServicesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: builtins.bool = ...

        def __init__(self, *, key: typing.Text=..., value: builtins.bool=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...

    class InputControllersEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...

        @property
        def value(self) -> global___InputControllerStatus:
            ...

        def __init__(self, *, key: typing.Text=..., value: typing.Optional[global___InputControllerStatus]=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...

    class GantriesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...

        @property
        def value(self) -> global___GantryStatus:
            ...

        def __init__(self, *, key: typing.Text=..., value: typing.Optional[global___GantryStatus]=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...
    ARMS_FIELD_NUMBER: builtins.int
    BASES_FIELD_NUMBER: builtins.int
    GRIPPERS_FIELD_NUMBER: builtins.int
    BOARDS_FIELD_NUMBER: builtins.int
    CAMERAS_FIELD_NUMBER: builtins.int
    SENSORS_FIELD_NUMBER: builtins.int
    FUNCTIONS_FIELD_NUMBER: builtins.int
    SERVOS_FIELD_NUMBER: builtins.int
    MOTORS_FIELD_NUMBER: builtins.int
    SERVICES_FIELD_NUMBER: builtins.int
    INPUT_CONTROLLERS_FIELD_NUMBER: builtins.int
    GANTRIES_FIELD_NUMBER: builtins.int

    @property
    def arms(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___ArmStatus]:
        ...

    @property
    def bases(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, builtins.bool]:
        ...

    @property
    def grippers(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, builtins.bool]:
        ...

    @property
    def boards(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, proto.api.common.v1.common_pb2.BoardStatus]:
        ...

    @property
    def cameras(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, builtins.bool]:
        ...

    @property
    def sensors(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___SensorStatus]:
        ...

    @property
    def functions(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, builtins.bool]:
        ...

    @property
    def servos(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___ServoStatus]:
        ...

    @property
    def motors(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___MotorStatus]:
        ...

    @property
    def services(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, builtins.bool]:
        ...

    @property
    def input_controllers(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___InputControllerStatus]:
        ...

    @property
    def gantries(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___GantryStatus]:
        ...

    def __init__(self, *, arms: typing.Optional[typing.Mapping[typing.Text, global___ArmStatus]]=..., bases: typing.Optional[typing.Mapping[typing.Text, builtins.bool]]=..., grippers: typing.Optional[typing.Mapping[typing.Text, builtins.bool]]=..., boards: typing.Optional[typing.Mapping[typing.Text, proto.api.common.v1.common_pb2.BoardStatus]]=..., cameras: typing.Optional[typing.Mapping[typing.Text, builtins.bool]]=..., sensors: typing.Optional[typing.Mapping[typing.Text, global___SensorStatus]]=..., functions: typing.Optional[typing.Mapping[typing.Text, builtins.bool]]=..., servos: typing.Optional[typing.Mapping[typing.Text, global___ServoStatus]]=..., motors: typing.Optional[typing.Mapping[typing.Text, global___MotorStatus]]=..., services: typing.Optional[typing.Mapping[typing.Text, builtins.bool]]=..., input_controllers: typing.Optional[typing.Mapping[typing.Text, global___InputControllerStatus]]=..., gantries: typing.Optional[typing.Mapping[typing.Text, global___GantryStatus]]=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['arms', b'arms', 'bases', b'bases', 'boards', b'boards', 'cameras', b'cameras', 'functions', b'functions', 'gantries', b'gantries', 'grippers', b'grippers', 'input_controllers', b'input_controllers', 'motors', b'motors', 'sensors', b'sensors', 'services', b'services', 'servos', b'servos']) -> None:
        ...
global___Status = Status

class ComponentConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    PARENT_FIELD_NUMBER: builtins.int
    POSE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    type: typing.Text = ...
    parent: typing.Text = ...

    @property
    def pose(self) -> global___Pose:
        ...

    def __init__(self, *, name: typing.Text=..., type: typing.Text=..., parent: typing.Text=..., pose: typing.Optional[global___Pose]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['pose', b'pose']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name', 'parent', b'parent', 'pose', b'pose', 'type', b'type']) -> None:
        ...
global___ComponentConfig = ComponentConfig

class ConfigRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self) -> None:
        ...
global___ConfigRequest = ConfigRequest

class ConfigResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    COMPONENTS_FIELD_NUMBER: builtins.int

    @property
    def components(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ComponentConfig]:
        ...

    def __init__(self, *, components: typing.Optional[typing.Iterable[global___ComponentConfig]]=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['components', b'components']) -> None:
        ...
global___ConfigResponse = ConfigResponse

class DoActionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...

    def __init__(self, *, name: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___DoActionRequest = DoActionRequest

class DoActionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self) -> None:
        ...
global___DoActionResponse = DoActionResponse

class GantryStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    POSITIONS_FIELD_NUMBER: builtins.int
    LENGTHS_FIELD_NUMBER: builtins.int

    @property
    def positions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        ...

    @property
    def lengths(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        ...

    def __init__(self, *, positions: typing.Optional[typing.Iterable[builtins.float]]=..., lengths: typing.Optional[typing.Iterable[builtins.float]]=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['lengths', b'lengths', 'positions', b'positions']) -> None:
        ...
global___GantryStatus = GantryStatus

class ArmStatus(google.protobuf.message.Message):
    """Arm

    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    GRID_POSITION_FIELD_NUMBER: builtins.int
    JOINT_POSITIONS_FIELD_NUMBER: builtins.int

    @property
    def grid_position(self) -> global___Pose:
        ...

    @property
    def joint_positions(self) -> global___JointPositions:
        ...

    def __init__(self, *, grid_position: typing.Optional[global___Pose]=..., joint_positions: typing.Optional[global___JointPositions]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['grid_position', b'grid_position', 'joint_positions', b'joint_positions']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['grid_position', b'grid_position', 'joint_positions', b'joint_positions']) -> None:
        ...
global___ArmStatus = ArmStatus

class Pose(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    O_X_FIELD_NUMBER: builtins.int
    O_Y_FIELD_NUMBER: builtins.int
    O_Z_FIELD_NUMBER: builtins.int
    THETA_FIELD_NUMBER: builtins.int
    x: builtins.float = ...
    'millimeters of the end effector from the base'
    y: builtins.float = ...
    z: builtins.float = ...
    o_x: builtins.float = ...
    'ox, oy, oz, theta represents an orientation vector\n    Structured similarly to an angle axis, an orientation vector works differently. Rather than representing an orientation\n    with an arbitrary axis and a rotation around it from an origin, an orientation vector represents orientation\n    such that the ox/oy/oz components represent the point on the cartesian unit sphere at which your end effector is pointing\n    from the origin, and that unit vector forms an axis around which theta rotates. This means that incrementing/decrementing\n    theta will perform an in-line rotation of the end effector.\n    Theta is defined as rotation between two planes: the plane defined by the origin, the point (0,0,1), and the rx,ry,rz\n    point, and the plane defined by the origin, the rx,ry,rz point, and the new local Z axis. So if theta is kept at\n    zero as the north/south pole is circled, the Roll will correct itself to remain in-line.\n    Theta in pb.Pose should be degrees. It will be converted to radians in the internal OrientationVec.\n    '
    o_y: builtins.float = ...
    o_z: builtins.float = ...
    theta: builtins.float = ...

    def __init__(self, *, x: builtins.float=..., y: builtins.float=..., z: builtins.float=..., o_x: builtins.float=..., o_y: builtins.float=..., o_z: builtins.float=..., theta: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['o_x', b'o_x', 'o_y', b'o_y', 'o_z', b'o_z', 'theta', b'theta', 'x', b'x', 'y', b'y', 'z', b'z']) -> None:
        ...
global___Pose = Pose

class JointPositions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEGREES_FIELD_NUMBER: builtins.int

    @property
    def degrees(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        ...

    def __init__(self, *, degrees: typing.Optional[typing.Iterable[builtins.float]]=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['degrees', b'degrees']) -> None:
        ...
global___JointPositions = JointPositions

class SensorStatus(google.protobuf.message.Message):
    """Sensor

    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TYPE_FIELD_NUMBER: builtins.int
    type: typing.Text = ...

    def __init__(self, *, type: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['type', b'type']) -> None:
        ...
global___SensorStatus = SensorStatus

class ExecuteFunctionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    'TODO(https://github.com/viamrobotics/rdk/issues/408): arguments'

    def __init__(self, *, name: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___ExecuteFunctionRequest = ExecuteFunctionRequest

class ExecuteFunctionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESULTS_FIELD_NUMBER: builtins.int
    STD_OUT_FIELD_NUMBER: builtins.int
    STD_ERR_FIELD_NUMBER: builtins.int

    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.struct_pb2.Value]:
        ...
    std_out: typing.Text = ...
    std_err: typing.Text = ...

    def __init__(self, *, results: typing.Optional[typing.Iterable[google.protobuf.struct_pb2.Value]]=..., std_out: typing.Text=..., std_err: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['results', b'results', 'std_err', b'std_err', 'std_out', b'std_out']) -> None:
        ...
global___ExecuteFunctionResponse = ExecuteFunctionResponse

class ExecuteSourceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SOURCE_FIELD_NUMBER: builtins.int
    ENGINE_FIELD_NUMBER: builtins.int
    source: typing.Text = ...
    engine: typing.Text = ...

    def __init__(self, *, source: typing.Text=..., engine: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['engine', b'engine', 'source', b'source']) -> None:
        ...
global___ExecuteSourceRequest = ExecuteSourceRequest

class ExecuteSourceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESULTS_FIELD_NUMBER: builtins.int
    STD_OUT_FIELD_NUMBER: builtins.int
    STD_ERR_FIELD_NUMBER: builtins.int

    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.struct_pb2.Value]:
        ...
    std_out: typing.Text = ...
    std_err: typing.Text = ...

    def __init__(self, *, results: typing.Optional[typing.Iterable[google.protobuf.struct_pb2.Value]]=..., std_out: typing.Text=..., std_err: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['results', b'results', 'std_err', b'std_err', 'std_out', b'std_out']) -> None:
        ...
global___ExecuteSourceResponse = ExecuteSourceResponse

class MotorStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ON_FIELD_NUMBER: builtins.int
    POSITION_SUPPORTED_FIELD_NUMBER: builtins.int
    POSITION_FIELD_NUMBER: builtins.int
    PID_CONFIG_FIELD_NUMBER: builtins.int
    on: builtins.bool = ...
    'To D0 (FA): Delete this field'
    position_supported: builtins.bool = ...
    'Returns true if the motor has position support'
    position: builtins.float = ...
    'Returns current position of the motor relative to its home'

    @property
    def pid_config(self) -> google.protobuf.struct_pb2.Struct:
        """To Do (FA): Delete this field"""
        pass

    def __init__(self, *, on: builtins.bool=..., position_supported: builtins.bool=..., position: builtins.float=..., pid_config: typing.Optional[google.protobuf.struct_pb2.Struct]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['_pid_config', b'_pid_config', 'pid_config', b'pid_config']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['_pid_config', b'_pid_config', 'on', b'on', 'pid_config', b'pid_config', 'position', b'position', 'position_supported', b'position_supported']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['_pid_config', b'_pid_config']) -> typing.Optional[typing_extensions.Literal['pid_config']]:
        ...
global___MotorStatus = MotorStatus

class ServoStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ANGLE_FIELD_NUMBER: builtins.int
    angle: builtins.int = ...

    def __init__(self, *, angle: builtins.int=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['angle', b'angle']) -> None:
        ...
global___ServoStatus = ServoStatus

class ResourceRunCommandRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    COMMAND_NAME_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    'Note(erd): okay in v1 because names are unique. v2 should be a VRN'
    command_name: typing.Text = ...

    @property
    def args(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, resource_name: typing.Text=..., command_name: typing.Text=..., args: typing.Optional[google.protobuf.struct_pb2.Struct]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['args', b'args']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['args', b'args', 'command_name', b'command_name', 'resource_name', b'resource_name']) -> None:
        ...
global___ResourceRunCommandRequest = ResourceRunCommandRequest

class ResourceRunCommandResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESULT_FIELD_NUMBER: builtins.int

    @property
    def result(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, result: typing.Optional[google.protobuf.struct_pb2.Struct]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['result', b'result']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['result', b'result']) -> None:
        ...
global___ResourceRunCommandResponse = ResourceRunCommandResponse

class NavigationServiceModeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self) -> None:
        ...
global___NavigationServiceModeRequest = NavigationServiceModeRequest

class NavigationServiceModeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MODE_FIELD_NUMBER: builtins.int
    mode: global___NavigationServiceMode.ValueType = ...

    def __init__(self, *, mode: global___NavigationServiceMode.ValueType=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['mode', b'mode']) -> None:
        ...
global___NavigationServiceModeResponse = NavigationServiceModeResponse

class NavigationServiceSetModeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MODE_FIELD_NUMBER: builtins.int
    mode: global___NavigationServiceMode.ValueType = ...

    def __init__(self, *, mode: global___NavigationServiceMode.ValueType=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['mode', b'mode']) -> None:
        ...
global___NavigationServiceSetModeRequest = NavigationServiceSetModeRequest

class NavigationServiceSetModeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self) -> None:
        ...
global___NavigationServiceSetModeResponse = NavigationServiceSetModeResponse

class NavigationServiceWaypoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    LOCATION_FIELD_NUMBER: builtins.int
    id: typing.Text = ...

    @property
    def location(self) -> proto.api.common.v1.common_pb2.GeoPoint:
        ...

    def __init__(self, *, id: typing.Text=..., location: typing.Optional[proto.api.common.v1.common_pb2.GeoPoint]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['location', b'location']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['id', b'id', 'location', b'location']) -> None:
        ...
global___NavigationServiceWaypoint = NavigationServiceWaypoint

class NavigationServiceLocationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self) -> None:
        ...
global___NavigationServiceLocationRequest = NavigationServiceLocationRequest

class NavigationServiceLocationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LOCATION_FIELD_NUMBER: builtins.int

    @property
    def location(self) -> proto.api.common.v1.common_pb2.GeoPoint:
        ...

    def __init__(self, *, location: typing.Optional[proto.api.common.v1.common_pb2.GeoPoint]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['location', b'location']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['location', b'location']) -> None:
        ...
global___NavigationServiceLocationResponse = NavigationServiceLocationResponse

class NavigationServiceWaypointsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self) -> None:
        ...
global___NavigationServiceWaypointsRequest = NavigationServiceWaypointsRequest

class NavigationServiceWaypointsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WAYPOINTS_FIELD_NUMBER: builtins.int

    @property
    def waypoints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NavigationServiceWaypoint]:
        ...

    def __init__(self, *, waypoints: typing.Optional[typing.Iterable[global___NavigationServiceWaypoint]]=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['waypoints', b'waypoints']) -> None:
        ...
global___NavigationServiceWaypointsResponse = NavigationServiceWaypointsResponse

class NavigationServiceAddWaypointRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LOCATION_FIELD_NUMBER: builtins.int

    @property
    def location(self) -> proto.api.common.v1.common_pb2.GeoPoint:
        ...

    def __init__(self, *, location: typing.Optional[proto.api.common.v1.common_pb2.GeoPoint]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['location', b'location']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['location', b'location']) -> None:
        ...
global___NavigationServiceAddWaypointRequest = NavigationServiceAddWaypointRequest

class NavigationServiceAddWaypointResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self) -> None:
        ...
global___NavigationServiceAddWaypointResponse = NavigationServiceAddWaypointResponse

class NavigationServiceRemoveWaypointRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    id: typing.Text = ...

    def __init__(self, *, id: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['id', b'id']) -> None:
        ...
global___NavigationServiceRemoveWaypointRequest = NavigationServiceRemoveWaypointRequest

class NavigationServiceRemoveWaypointResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self) -> None:
        ...
global___NavigationServiceRemoveWaypointResponse = NavigationServiceRemoveWaypointResponse

class InputControllerEvent(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TIME_FIELD_NUMBER: builtins.int
    EVENT_FIELD_NUMBER: builtins.int
    CONTROL_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int

    @property
    def time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...
    event: typing.Text = ...
    'An event type (eg: ButtonPress, ButtonRelease)'
    control: typing.Text = ...
    'A control, can be a button (eg: ButtonSouth) or an axis (eg: AbsoluteX)'
    value: builtins.float = ...
    '0 or 1 for buttons, -1.0 to +1.0 for axes'

    def __init__(self, *, time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp]=..., event: typing.Text=..., control: typing.Text=..., value: builtins.float=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['time', b'time']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['control', b'control', 'event', b'event', 'time', b'time', 'value', b'value']) -> None:
        ...
global___InputControllerEvent = InputControllerEvent

class InputControllerStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    EVENTS_FIELD_NUMBER: builtins.int

    @property
    def events(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___InputControllerEvent]:
        ...

    def __init__(self, *, events: typing.Optional[typing.Iterable[global___InputControllerEvent]]=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['events', b'events']) -> None:
        ...
global___InputControllerStatus = InputControllerStatus