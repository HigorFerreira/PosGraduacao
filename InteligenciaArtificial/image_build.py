from hanoi_lib.types import Block

def svg_head(width=160, height=120, child=""):
    return f"""
    <svg
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 {width} {height}"
        >
        {child}
    </svg>
    """

def head(x=0, y=0, child="", label=""):
    label_txt = "" if not label else f"""
    \r<text x="10" y="7" font-size="5">
        \r{label}
    \r</text>"""
    
    return f"""
    <g>
        <g transform="translate({x},{y})">
            <rect width="160" height="120" style="fill:white" />
            
            <g transform="translate(0,120) scale(1,-1)">
                { child }    
            </g>
        </g>
        { label_txt }
    </g>
    """

def plot_tower(tower: list[Block], id: str, x: int, y: int):
    colors = {
        "4": "blue",
        "3": "red",
        "2": "yellow",
        "1": "pink",
    }

    sep = "\n\t\t\t"

    def process(obj: tuple[int, Block]):
        i, block = obj
        x = -0.5*(block*10)+20
        return f'<rect x="{x}" y="{5+i*15}" width="{block*10}" height="10" style="fill:{colors[str(block)]}" />'

    return f"""
    <g id="{id}" transform="translate({x},{y})">
        <rect width="5" height="80" />

        <g transform="translate(-17.5,0)">
            {sep.join(list(map(lambda obj: process(obj), enumerate(tower))))}
        </g>
    </g>
    """

def plot_game(towers: list[list[Block]], label=""):
    labels = { 0: 'A', 1: 'B', 2: 'C' }
    sep="\n\t\t"
    def process(obj: tuple[int, list]):
        i, item = obj
        return plot_tower(item, f"Tower{labels[i]}", 30+i*50, 0)
    
    return svg_head(
        child=head(
            0, 0,
            sep.join(
                list(
                    map(
                        lambda obj: process(obj),
                        enumerate(towers)
                    )
                )
            ),
            label=label
        )
    )