def generate_movements(parsed_paths: list) -> list:
    """
    Convert Path objects into movement instructions which the AxiDraw plotter understands.
    
    Args:
        parsed_paths (list): List of parsed SVG Path objects.
    
    Returns:
        list: A list of movement commands as tuples ('move_to', x, y) and ('line_to', x, y).
    """
    movements = []
    
    for path in parsed_paths:
        for segment in path:
            # Check if the segment has start and end points
            # if so, append 'move_to' and 'line_to' instructions.
            if hasattr(segment, 'start') and hasattr(segment, 'end'):
                start, end = segment.start, segment.end
                movements.append(('move_to', start.real, start.imag))
                movements.append(('line_to', end.real, end.imag))
    
    return movements
