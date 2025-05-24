from hlib import Block

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

def head(x=0, y=0, child=""):
    return f"""
    <g transform="translate({x},{y})">
        <rect width="160" height="120" style="fill:white" />
        <rect x="10" y="10" width="145" height="100" style="fill:white;stroke:black;stroke-width:0.5" />
        
        <g transform="translate(0,120) scale(1,-1)">
            { child }    
        </g>
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

    return f"""
    <g id="{id}" transform="translate({x},{y})">
        <rect width="5" height="80" />

        <g transform="translate(-17.5,0)">
            {sep.join(list(map(lambda obj: f'<rect x="{obj[0]*5}" y="{5+obj[0]*15}" width="{obj[1]*10}" height="10" style="fill:{colors[str(obj[1])]}" />', enumerate(tower))))}
        </g>
    </g>
    """

def plot_game(towers: list[list[Block]]):
    return svg_head(
        child=head(
            0, 0,
            "\n\t\t".join(
                list(
                    map(
                        lambda cur: plot_tower(cur[1],
                        f"Tower{cur[0]}", 30+cur[0]*50, 0),
                        enumerate(towers)
                    )
                )
            )
        )
    )