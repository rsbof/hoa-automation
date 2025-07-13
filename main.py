import argparse
import arena
import grand_market

def main():
    parser = argparse.ArgumentParser(prog='hoa-automation')
    subparsers = parser.add_subparsers(title='subcommands',
                                       dest='subparser',
                                       help='subcommand help')

    arena_parser = subparsers.add_parser('arena')
    arena_parser.add_argument('command')

    market_parser = subparsers.add_parser('market')
    market_parser.add_argument('command')

    args = parser.parse_args()
    match (args.subparser):
        case 'arena':
            arena.run(args)
        case 'market':
            grand_market.run(args)
        case _:
            raise ValueError(f"the command '{args.subparser}' does not supported.")

if __name__ == "__main__":
    main()
