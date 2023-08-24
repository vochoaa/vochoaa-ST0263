 #Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc


import files_pb2 as files__pb2


class FilesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetFilesList = channel.unary_unary(
                '/Files/GetFilesList',
                request_serializer=files__pb2.ListFilesRequest.SerializeToString,
                response_deserializer=files__pb2.ListFilesResponse.FromString,
                )
        self.SearchFiles = channel.unary_unary(
                '/Files/SearchFiles',
                request_serializer=files__pb2.SearchFilesRequest.SerializeToString,
                response_deserializer=files__pb2.SearchFilesResponse.FromString,
                )


class FilesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetFilesList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FilesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetFilesList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFilesList,
                    request_deserializer=files__pb2.ListFilesRequest.FromString,
                    response_serializer=files__pb2.ListFilesResponse.SerializeToString,
            ),
            'SearchFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchFiles,
                    request_deserializer=files__pb2.SearchFilesRequest.FromString,
                    response_serializer=files__pb2.SearchFilesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Files', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Files(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetFilesList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Files/GetFilesList',
            files__pb2.ListFilesRequest.SerializeToString,
            files__pb2.ListFilesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Files/SearchFiles',
            files__pb2.SearchFilesRequest.SerializeToString,
            files__pb2.SearchFilesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)