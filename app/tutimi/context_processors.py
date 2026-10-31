from django.conf import settings


def site_metadata(request):
  return {
      'CONTACT_EMAIL': settings.CONTACT_EMAIL,
      'LINKEDIN_URL': settings.LINKEDIN_URL,
      'GITHUB_URL': settings.GITHUB_URL,
  }