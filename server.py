# try:
import grpc, django, os, sys, django
from User.protos import profile_pb2, profile_pb2_grpc
from concurrent import futures
from dotenv import load_dotenv
from gRPC_project.settings import BASE_DIR

try:
    load_dotenv()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gRPC_project.settings")
    project_path=BASE_DIR
    if project_path:
        sys.path.extend([project_path])
        if 'setup' in dir(django):
            django.setup()
    else:
        raise ImportError("DJANGO_PROJECT_FULL_PATH environment variable not set.")


except ModuleNotFoundError as e:
    print(f"Error: {e}")
    sys.exit(1)

try:
    from User.models import ConsoleUser
    from User.protos import profile_pb2, profile_pb2_grpc
except ModuleNotFoundError as e:
    print(f"Error: {e}")
    sys.exit(1)


class ProfileService(profile_pb2_grpc.ProfileServiceServicer):
    def CreateProfile(self, request, context):
        try:
            first_name= request.first_name
            last_name= request.last_name
            email= request.email
            ConsoleUser.objects.create(first_name = first_name,last_name =last_name, email = email)
            response= profile_pb2.CreateProfileResponse(
                status=200,
                msg="profile created"
            )
            return response
        except Exception as e:
            print(f"error- {e}")
            response = profile_pb2.CreateProfileResponse(
                status=400,
                msg=" Invalid Request not enough credentials",
                error =str(e)
            )
            return response



def serve():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=6))
    profile_pb2_grpc.add_ProfileServiceServicer_to_server(ProfileService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("server started")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()


