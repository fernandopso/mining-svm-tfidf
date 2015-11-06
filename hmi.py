# !/usr/bin/env python
# -*- coding: utf-8 -*-
from app.collector.collect import Collect
from app.miner.mining import Mining
from app.storer.storage import Storage
from app.trainer.training import Training
from app.cli import Cli

if __name__ == '__main__':
    """
    Human-Machine Interface
    """
    cli = Cli()
    cli.clear_terminal()
    cli.dashboard()
    cli.waiting_input()

    while cli.option != 'x':
        if cli.option == 'h':
            cli.clear_terminal()
            cli.help()

        elif cli.option == 'c':
            if not cli.args:
                cli.error(cli.option)
            else:
                c = Collect(cli.args[0])
                c.connect_with_twitter()
                tweets = c.search_tweets()
                storage = Storage(tweets, 'collected')
                storage.save()
                cli.success(cli.option)

        elif cli.option == 't':
            # Load files
            data = Storage([], 'collected').load()

            # Training of tweets
            tweets = Training(data).evaluate()

            # Save tweets
            Storage(tweets, 'trained').save()

        elif cli.option == 'p':
            collect_files = Storage([], 'collected').load()
            trained_files = Storage([], 'trained').load()

            Mining(collect_files, trained_files).start()

        # TODO: Use command options and arguments
        elif cli.option == 'tweets':
            data = Storage([], 'collected').load()
            cli.tweets_colleted(data)

        elif cli.option == 'tweets trained':
            data = Storage([], 'trained').load()
            cli.tweets_trained(data)

        elif cli.option == 'tweets trained positive':
            data = Storage([], 'trained').load()
            cli.tweets_trained(data, '1')

        elif cli.option == 'tweets trained negative':
            data = Storage([], 'trained').load()
            cli.tweets_trained(data, '2')

        elif cli.option == 'tweets trained neutral':
            data = Storage([], 'trained').load()
            cli.tweets_trained(data, '3')

        elif cli.option == 'tweets trained unknown':
            data = Storage([], 'trained').load()
            cli.tweets_trained(data, '4')

        elif cli.option == 'tweets metrics':
            collected = Storage([], 'collected').load()
            trained   = Storage([], 'trained').load()
            cli.tweets_metrics(collected, trained)

        cli.waiting_input()

    cli.finished()