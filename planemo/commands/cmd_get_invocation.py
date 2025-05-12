"""Module describing the planemo ``list_invocations`` command."""

import json

import click

from bioblend.galaxy import GalaxyInstance
from bioblend.galaxy.invocations import InvocationClient

from planemo import options
from planemo.cli import command_function
from planemo.galaxy import profiles


try:
    from tabulate import tabulate
except ImportError:
    tabulate = None  # type: ignore


@click.command("get_invocation")
@click.argument(
    "invocation_identifier",
    type=click.STRING,
)
@options.profile_option(required=True)
@command_function
def cli(ctx, invocation_identifier, **kwds):
    """
    Get information about an invocation.
    """
    profile = profiles.ensure_profile(ctx, kwds.get("profile"))
    
    gi =  GalaxyInstance(url=profile["galaxy_url"], key=profile["galaxy_admin_key"] or profile["galaxy_user_key"])
    invocation_client = InvocationClient(gi)

    invocation_data = invocation_client.show_invocation(invocation_identifier)
    print(json.dumps(invocation_data))
    return
