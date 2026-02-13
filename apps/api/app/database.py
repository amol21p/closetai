from supabase import create_client, Client
from app.config import get_settings


def get_supabase() -> Client:
    settings = get_settings()
    return create_client(settings.supabase_url, settings.supabase_key)


def get_supabase_admin() -> Client:
    """Admin client with service role key - bypasses RLS."""
    settings = get_settings()
    return create_client(settings.supabase_url, settings.supabase_service_key)
