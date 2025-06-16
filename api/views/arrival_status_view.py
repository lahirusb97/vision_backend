from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from ..models import Order, ExternalLensArrivalStatus
from ..serializers import ExternalLensArrivalStatusSerializer

class ExternalLensArrivalStatusBulkCreateView(APIView):
    """Bulk create ExternalLensArrivalStatus records."""

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = request.data
        if not isinstance(data, list):
            return Response({"error": "Expected a list of objects."}, status=status.HTTP_400_BAD_REQUEST)

        created = []
        for item in data:
            order_id = item.get("order_id")
            external_lens_id = item.get("external_lens_id")
            if order_id is None or external_lens_id is None:
                return Response({"error": "order_id and external_lens_id are required."}, status=status.HTTP_400_BAD_REQUEST)
            try:
                order = Order.objects.get(pk=order_id)
            except Order.DoesNotExist:
                return Response({"error": f"Order {order_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)

            status_obj = ExternalLensArrivalStatus.objects.create(
                order=order,
                external_lens_id=external_lens_id,
                arrival_status="received",
            )
            created.append(ExternalLensArrivalStatusSerializer(status_obj).data)

        return Response(created, status=status.HTTP_201_CREATED)
