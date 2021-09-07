from . import Arc, Handle
from pygame.sprite import LayeredUpdates


class PieChart:
    chart = None

    @classmethod
    def init(cls, cx, cy, values):
        cls.chart = LayeredUpdates()

        a, b = 0, 0
        arcs, handles = [], []
        for name in values:
            color = values[name]['color']
            value = values[name]['value']
            handle_color = values[name]['handle']

            b += round((value / 100) * 360)

            arc = Arc(name, color, a, b, 74)
            handle = Handle(b, arc.handle_pos, handle_color)

            cls.chart.add(arc, layer=1)
            cls.chart.add(handle, layer=2)
            arcs.append(arc)
            handles.append(handle)
            a = b

        arcs[0].links(handles[2], handles[0])
        arcs[1].links(handles[0], handles[1])
        arcs[2].links(handles[1], handles[2])

        arcs[0].displace(cx, cy)
        arcs[1].displace(cx, cy)
        arcs[2].displace(cx, cy)

    @classmethod
    def draw(cls, fondo):
        cls.chart.update()
        cls.chart.draw(fondo)

    @classmethod
    def get_value(cls, name):
        arc = [spr for spr in cls.chart.get_sprites_from_layer(1) if spr.name == name][0]
        return arc.get_value()
