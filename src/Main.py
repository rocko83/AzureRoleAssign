from LerJson import LerJson as Lj
import argparse


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--config',
                        required=True,
                        action='store',
                        help='Arquivo de configuração, JSON')
    parser.add_argument('--tipo',
                        required=True,
                        action='store',
                        help='Tipo do grupo: grupo | key')

    args = parser.parse_args()

    return args

args=get_args()
dados = Lj(args.config,args.tipo)
dados.getAzCommands()