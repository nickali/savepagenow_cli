import click
import savepagenow
import pyperclip

@click.command()
@click.argument('url')
@click.option('-ua', '--user-agent', default=None, help='User-Agent header for the web request')
@click.option('-c', '--accept-cache', is_flag=True, help='Accept and return cached URL')
@click.option('-a', '--authenticate', is_flag=True, help='Allows you to run saves with authentication')
def cli(url, user_agent, accept_cache, authenticate):
    """Archive the provided URL using archive.org's Wayback Machine."""
    try:
        if accept_cache:
            archive_url, captured = savepagenow.capture_or_cache(url, user_agent=user_agent, authenticate=authenticate)
            print(f"URL: {archive_url} (Captured: {captured})")
        else:
            archive_url = savepagenow.capture(url, user_agent=user_agent, authenticate=authenticate)
            print(f"URL: {archive_url}")
        
        # Copy the archive URL to the clipboard
        pyperclip.copy(archive_url)
        print("The archive URL has been copied to the clipboard.")
    except savepagenow.exceptions.CachedPage as e:
        print(f"CachedPage Exception: {e}")

if __name__ == '__main__':
    cli()
