from pathlib import Path
import yaml

def _yaml_location(path, exc):
    mark = getattr(exc, 'problem_mark', None)
    line = getattr(mark, 'line', None)
    if line is not None:
        column = getattr(mark, 'column', None)
        where = f'{path.name}:{line + 1}:{1 if column is None else column + 1}'
    else:
        where = path.name
    detail = getattr(exc, 'problem', None) or str(exc).splitlines()[0]
    return f'{where}: {detail}
