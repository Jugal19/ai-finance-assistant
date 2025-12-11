from utils.pdf_generator import generate_report
from controllers.ai_controller import AIController
from controllers.dashboard_controller import DashboardController

class ReportController:

    @staticmethod
    async def generate_report(user):
        summary = await DashboardController.summary(user)
        insights = await AIController.insights(user)

        text = {
            f"Monthly Report \n\n"
            f"Income: {summary['income']}\n"
            f"Expenses: {summary['expenses']}\n"
            f"Net: {summary['net']}\n\n"
            f"AI Insights: {insights['insights']}\n"
        }

        filename = generate_report(text)
        return {"report": filename}