import argparse
import csv
import pprint
import sys

from checkin import CheckIn
from checkin_timeline import CheckInTimeline
from pokeball import Pokeball


def load_timeline(filename):
    """Loads a CSV file of Team Rocket agent checkins.

    :param str filename: The name of the CSV file to read

    :returns: A tuple with the following pokemon:

                - A dictionary that maps an agent's name to the
                  Pokemon they stored in their initial Pokeball
                  (based on data in the CSV file).

                - A CheckInTimeline that contains the check-in
                  data loaded from the CSV file.

    :rtype: tuple

    :raises ValueError: If there is an issue unpacking the values of a
        row into name, pokeball type, location, time, and
        pokemon. Note that this is thrown when unpacking too few or
        two many values into a tuple of variables.

    :raises ValueError: If there is an issue loading the time (fourth
        column in each row) into a datetime object.

    :raises ValueError: If there is an issue loading the type of
        Pokeball (second column in each row, stored as the integer
        value of a :class:`Pokeball <pokeball.Pokeball>` enum)

    :raises OSError: If there is an issue finding or opening the
        file. Note that this is thrown by the open() function.

    """
    my_dict = {}
    timeline = CheckInTimeline()

    with open(filename) as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            # Put agent name and initial Pokemon into a dictionary
            # Row index: 0 = name, 1 = ball type, 2 = location, 3 = time
            name, ball_type, location, time, init_poke = row
            if init_poke != '':
                my_dict[name] = init_poke

            # Read data to checkins
            input = (name, Pokeball(int(ball_type)), location, time)
            checkin = CheckIn(*input)

            # Add checkin to timeline
            timeline.add(checkin)

    return (my_dict, timeline)


def main(args):
    """Program entry point.

    - Loads a CSV file of checkins

    - Determines how Pokemon were exchanged during various rendezvous

    - Outputs information to the console

      - Prints the exchanges as they happen if desired.

      - Prints the latest agent to be in posession of a *specific*
        pokemon if desired.

      - Otherwise, neatly prints a dictionary mapping agents to the
        pokemon they have carried most recently.

    This program will return an exit code of ``1`` in one of the
    following situations:

    - If the CSV file cannot be opened (i.e., load_timeline raises an
      :class:`OSError`), this program will simply print the exception
      and end.

    - If the CSV file cannot be loaded (i.e., load_timeline raises a
      :class:`ValueError`), we will print an error messsage and end.

    - If the CSV file contains semantically incorrect data (i.e., a
      :class:`DataError <checkin_timeline.DataError>` is raised), we
      will print an error messsage and end.

    :param argparse.Namespace args: A Namespace that contains parsed
        command line arguments.

    :returns: None

    """
    # Try to unpack dictionary and timeline, otherwise catch errors.
    try:
        dict, timeline = load_timeline(args.checkins)
    except OSError as e:
        print(e)
        sys.exit(1)
    except ValueError:
        print('ValueError: Problem loading data from a row in the file.')
        sys.exit(1)
    except DataError:
        print('DataError: semantically incorrect data, abort.')
        sys.exit(1)

    # --exchanges,: prints message when pokeballs were exchanged.
    if args.exchanges is True:
        # Check if each p1 and p2 have same pokeball type.
        for p1, p2 in timeline.rendezvous():
            if p1.pokeball == p2.pokeball:
                n1 = p1.name
                n2 = p2.name
                msg = '{} meets with {} to exchange {} for {}'
                msg = msg.format(n1, n2, dict[n1], dict[n2])
                print(msg)

    # --skip: prints message when pokeballs were not exchanged.
    if args.skip is True:
        for p1, p2 in timeline.rendezvous():
        # Check if each p1 and p2 don't have same pokeball type.
            if p1.pokeball != p2.pokeball:
                name1 = p1.name
                name2 = p2.name
                msg = '{} (with {}) meets with {} (with {}), '
                msg += 'but nothing happened.'
                msg = msg.format(name1, p1.pokeball, name2, p2.pokeball)
                print(msg)

    # --pokemon: Checks who has the pokeball
    if args.pokemon != '':
        for key in dict.keys():
            if dict[key] == args.pokemon:
                break
        msg = '{} had the {}'
        msg = msg.format(key, args.pokemon)
        print(msg)

    # Pretty print the dictionary
    else:
        pp = pprint.PrettyPrinter(4)
        pp.pprint(dict)


if __name__ == '__main__':
    # Initialize CLI argument parser
    parser = argparse.ArgumentParser(
        description='Determine rendezvous exchanges based on a '
        'spreadsheet of agent check-ins.'
    )

    # Add a positional argument for the checkins file.
    parser.add_argument('checkins',
                        help='A CSV file to read checkins from.')

    # Add an optional flag, so that the user can tell us which Pokemon
    # they want to see the owner of
    parser.add_argument('--pokemon', type=str, default='',
                        help='Filter to show who has a specific Pokemon')

    # Add an optional flag, that will tell us to print exchanges as
    # they occur (only if an exchange *actually* occurs).
    parser.add_argument('--exchanges', action='store_true',
                        help='Print all exchanges')

    # Add an optional flag, so that the user can tell us if they want
    # to see a message whenever two Team Rocket agents meet, but they
    # **do not** swap Poke Balls.
    parser.add_argument('--skip', action='store_true',
                        help='Print skipped exchanges')

    # Parse the arguments
    args = parser.parse_args()

    # GO!
    main(args)
