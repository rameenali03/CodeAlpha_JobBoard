from rest_framework import generics
from .models import Application
from .serializers import ApplicationSerializer


class ApplicationListCreateView(generics.ListCreateAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        queryset = Application.objects.all().order_by("-applied_at")

        candidate = self.request.query_params.get("candidate")
        job = self.request.query_params.get("job")
        status = self.request.query_params.get("status")

        if candidate:
            queryset = queryset.filter(candidate_id=candidate)

        if job:
            queryset = queryset.filter(job_id=job)

        if status:
            queryset = queryset.filter(status=status)

        return queryset

class ApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
