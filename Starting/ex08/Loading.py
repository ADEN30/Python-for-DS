def my_tqdm(iterable):
    """
    A simplified version of tqdm to display a progress bar for an iterable.

    Args:
        iterable: An iterable to decorate with a progressbar.
        desc (str, optional): Prefix for the progressbar.
        total (int, optional): The number of expected iterations.

    Yields:
        Items from the iterable.
    """
    total = len(iterable)
    
    for i, item in enumerate(iterable, start=1):
        yield item

        # Calculate progress
        progress = i / total if total != "?" else 0
        progress_percent = progress * 100

        # Format the progress bar
        bar_length = 50
        block = int(round(bar_length * progress))
        progress_bar = "=" * (block - 1) + ">" + "-" * (bar_length - block)

        # Format the output line
        output = f"\r{progress_percent:3.0f}%|{progress_bar}| {i}/{total}"
        print(output, end='\r')


