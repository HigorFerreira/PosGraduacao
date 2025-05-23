from hlib import Block

def head(x=0, y=0, child=""):
    return f"""
    <g transform="translate({x},{y})">
        <rect width="160" height="120" style="fill:white" />
        <rect x="10" y="10" width="145" height="100" style="fill:white;stroke:black;stroke-width:0.5" />
        
        <g transform="translate(0,120) scale(1,-1)">
            <g id="torreA" transform="translate(30,10)">
                <rect width="5" height="80" />

                <g transform="translate(-17.5,0)">
                    <rect y="5" width="40" height="10" style="fill:blue" />
                    <rect x="5" y="20" width="30" height="10" style="fill:red" />
                    <rect x="10" y="35" width="20" height="10" style="fill:yellow" />
                    <rect x="15" y="50" width="10" height="10" style="fill:pink" />
                </g>
            </g>

            <g id="torreB" transform="translate(80,10)">
                <rect width="5" height="80" />

                <g transform="translate(-17.5,0)">
                    <rect y="5" width="40" height="10" style="fill:blue" />
                    <rect x="5" y="20" width="30" height="10" style="fill:red" />
                    <rect x="10" y="35" width="20" height="10" style="fill:yellow" />
                    <rect x="15" y="50" width="10" height="10" style="fill:pink" />
                </g>
            </g>

            <g id="torreC" transform="translate(130,10)">
                <rect width="5" height="80" />

                <g transform="translate(-17.5,0)">
                    <rect y="5" width="40" height="10" style="fill:blue" />
                    <rect x="5" y="20" width="30" height="10" style="fill:red" />
                    <rect x="10" y="35" width="20" height="10" style="fill:yellow" />
                    <rect x="15" y="50" width="10" height="10" style="fill:pink" />
                </g>
            </g>        
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

    return f"""
    <g id="{id}" transform="translate({x},{y})">
        <rect width="5" height="80" />

        <g transform="translate(-17.5,0)">
            {"\n".join(list(map(lambda obj: f'<rect x="{obj[0]*5}" y="5" width="{obj[1]*10}" height="10" style="fill:{colors[obj[1]]}" />', enumerate(tower))))}
            <rect x="0" y="5" width="40" height="10" style="fill:blue" />
            <rect x="5" y="20" width="30" height="10" style="fill:red" />
            <rect x="10" y="35" width="20" height="10" style="fill:yellow" />
            <rect x="15" y="50" width="10" height="10" style="fill:pink" />
        </g>
    </g>
    """