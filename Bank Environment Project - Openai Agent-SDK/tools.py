import random
from pydantic import BaseModel, Field
from agents import function_tool

class ServiceType(BaseModel):
    service: str
    confidence: float
    keywords_detected: list[str]
    reasoning: str

class ToolInfo(BaseModel):
    token_number: str
    wait_time: str
    message: str
    service_type: str

#---------------------------------------------------------------------------------
@function_tool
def identify_banking_purpose(customer_request: str):
    """It is a simple function to figure out what banking service customer needs."""

    request = customer_request.lower()

    if ("balance" in request) or ("statement" in request) or ("account" in request):
        return ServiceType(
            service = "account_service",
            confidence = 0.9,
            keywords_detected = ["balance", "statement", "account"],
            reasoning = "Customer wants to check their account balance"
        )
    elif ("transfer" in request) or ("send" in request) or ("payment" in request):
        return ServiceType(
            service = "transfer_service",
            confidence = 0.9,
            keywords_detected = ["transfer", "send", "payment"],
            reasoning = "Customer wants to send money or make payments"
        )
    elif ("loan" in request) or ("mortgage" in request) or ("borrow" in request):
        return ServiceType(
            service = "loan_service",
            confidence = 0.9,
            keywords_detected = ["loan", "mortgage", "borrow"],
            reasoning = "Customer wants information or need help about loans or mortgages"
        )
    else:
        return ServiceType(
            service = "general",
            confidence = 0.5,
            keywords_detected = ["general"],
            reasoning = "Customer request is general banking inquiry or needs general assistance"
        )

@function_tool
def generate_customer_token(service_type: str = "general")-> ToolInfo:
    """Generate a token number for the customer queue. The value of service_type argument can be only these as mention below.

    Args: service_type = general, service_type = account_service, service_type = transfer_service, service_type = loan_service
    """

    if service_type == "account_service":
        prefix = "ACC"
        wait_time = "5-10 minutes"
    elif service_type == "transfer_service":
        prefix = "TRF"
        wait_time = "2-5 minutes"
    elif service_type == "loan_service":
        prefix = "LOA"
        wait_time = "15-20 minutes"
    else:
        prefix = "GEN"
        wait_time = "10-15 minutes"

    token_number = f"{prefix}{random.randint(100, 999)}"

    return ToolInfo(
        token_number=token_number,
        wait_time=wait_time,
        message=f"Your token number is {token_number}. Please have a seat, and wait for {wait_time}. We will call you shortly!",
        service_type=service_type
    )
