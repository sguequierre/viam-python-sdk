from typing import List, Mapping, Optional

from grpclib.client import Channel

from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.service.slam import (
    GetInternalStateRequest,
    GetInternalStateResponse,
    GetPointCloudMapRequest,
    GetPointCloudMapResponse,
    GetPositionRequest,
    GetPositionResponse,
    GetPropertiesRequest,
    SLAMServiceStub,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, struct_to_dict

from . import Pose
from .slam import SLAM


class SLAMClient(SLAM, ReconfigurableResourceRPCClientBase):
    """
    Connect to the SLAMService, which allows the robot to create a map of its surroundings and find its location in that map.
    """

    client: SLAMServiceStub

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = SLAMServiceStub(channel)
        super().__init__(name)

    async def get_position(self, *, timeout: Optional[float] = None, **kwargs) -> Pose:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetPositionRequest(name=self.name)
        response: GetPositionResponse = await self.client.GetPosition(request, timeout=timeout, metadata=md)
        return response.pose

    async def get_point_cloud_map(self, return_edited_map: bool = False, *, timeout: Optional[float] = None, **kwargs) -> List[bytes]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetPointCloudMapRequest(name=self.name, return_edited_map=return_edited_map)
        response: List[GetPointCloudMapResponse] = await self.client.GetPointCloudMap(request, timeout=timeout, metadata=md)
        return [r.point_cloud_pcd_chunk for r in response]

    async def get_internal_state(self, *, timeout: Optional[float] = None, **kwargs) -> List[bytes]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetInternalStateRequest(name=self.name)
        response: List[GetInternalStateResponse] = await self.client.GetInternalState(request, timeout=timeout, metadata=md)
        return [r.internal_state_chunk for r in response]

    async def get_properties(self, *, timeout: Optional[float] = None, **kwargs) -> SLAM.Properties:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetPropertiesRequest(name=self.name)
        return await self.client.GetProperties(request, timeout=timeout, metadata=md)

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout, metadata=md)
        return struct_to_dict(response.result)
