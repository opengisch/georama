import os
from pathlib import Path


def profile_async(func):
    """A profiler which can be used as a decorator on ASYNC methods to produce
    profiles and call graphs.

    The Callgraph might be inspected with QCacheGrind or KCacheGrind or sth. else.

    Args:
        func: the wrapped method

    Returns:
        The wrapper
    """

    async def wrapper(*args, **kwargs):
        import cProfile
        import pstats

        import pyprof2calltree

        pr = cProfile.Profile()
        pr.enable()

        result = await func(*args, **kwargs)

        pr.disable()
        stats = pstats.Stats(pr)
        path = Path(".profile")
        path.mkdir(parents=True, exist_ok=True)
        stats_file = os.path.join(
            str(path), f"{func.__module__}.{func.__name__}.profile_data.prof"
        )
        callgrind_file = os.path.join(
            str(path), f"{func.__module__}.{func.__name__}.callgrind.out"
        )
        stats.dump_stats(stats_file)
        call_tree = pyprof2calltree.CalltreeConverter(stats)
        with open(callgrind_file, "w+") as f:
            call_tree.output(f)
        print(f"Profiling data saved to: {stats_file}, CallTree saved t: {callgrind_file}")

        return result

    return wrapper


def profile_sync(func):
    """A profiler which can be used as a decorator on SYNC methods to produce
    profiles and call graphs.

    The Callgraph might be inspected with QCacheGrind or KCacheGrind or sth. else.

    Args:
        func: the wrapped method

    Returns:
        The wrapper
    """

    def wrapper(*args, **kwargs):
        import cProfile
        import pstats

        import pyprof2calltree

        pr = cProfile.Profile()
        pr.enable()

        result = func(*args, **kwargs)

        pr.disable()
        stats = pstats.Stats(pr)
        path = Path(".profile")
        path.mkdir(parents=True, exist_ok=True)
        stats_file = os.path.join(
            str(path), f"{func.__module__}.{func.__name__}.profile_data.prof"
        )
        callgrind_file = os.path.join(
            str(path), f"{func.__module__}.{func.__name__}.callgrind.out"
        )
        stats.dump_stats(stats_file)
        call_tree = pyprof2calltree.CalltreeConverter(stats)
        with open(callgrind_file, "w+") as f:
            call_tree.output(f)
        print(f"Profiling data saved to: {stats_file}, " f"CallTree saved t: {callgrind_file}")

        return result

    return wrapper
