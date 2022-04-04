"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
from ...... import proto
import typing
import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetPosesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    BODY_NAMES_FIELD_NUMBER: builtins.int
    name: typing.Text
    'Name of the pose tracker'

    @property
    def body_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Names of the bodies whose poses are being requested. In the event
        this parameter is not supplied or is an empty list, all available
        poses are returned
        """
        pass

    def __init__(self, *, name: typing.Text=..., body_names: typing.Optional[typing.Iterable[typing.Text]]=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['body_names', b'body_names', 'name', b'name']) -> None:
        ...
global___GetPosesRequest = GetPosesRequest

class GetPosesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class BodyPosesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text

        @property
        def value(self) -> proto.api.common.v1.common_pb2.PoseInFrame:
            ...

        def __init__(self, *, key: typing.Text=..., value: typing.Optional[proto.api.common.v1.common_pb2.PoseInFrame]=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...
    BODY_POSES_FIELD_NUMBER: builtins.int

    @property
    def body_poses(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, proto.api.common.v1.common_pb2.PoseInFrame]:
        """Mapping of each body name to the pose representing the center of the body."""
        pass

    def __init__(self, *, body_poses: typing.Optional[typing.Mapping[typing.Text, proto.api.common.v1.common_pb2.PoseInFrame]]=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['body_poses', b'body_poses']) -> None:
        ...
global___GetPosesResponse = GetPosesResponse