import grpc
from User.protos import profile_pb2_grpc,profile_pb2


channel= grpc.insecure_channel('localhost:50051')
client=profile_pb2_grpc.ProfileServiceStub(channel)

request= profile_pb2.CreateProfileRequest(first_name="lets", last_name="do", email="this")
response =client.CreateProfile(request)
print(response.status,response.msg,response.error)
