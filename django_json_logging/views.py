import json
import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def log(request):
    logger.info("Sample info log")
    return HttpResponse(
        json.dumps({"status": "OK"}),
        headers={"content-type": "application/json"}
    )
