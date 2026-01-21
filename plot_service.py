
import io
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


FUNCTIONS = {
    "sin": lambda x: np.sin(x),
    "cos": lambda x: np.cos(x),
    "square": lambda x: signal.square(2 * np.pi * x),
    "triangle": lambda x: signal.sawtooth(2 * np.pi * x, width=0.5),
    "sawtooth": lambda x: signal.sawtooth(2 * np.pi * x),
}

def generate_function_plot(
    global_start: float,
    global_end: float,
    global_points: int,
    global_grid: bool,
    configs,
    title: str = None,
    xlabel: str = None,
    ylabel: str = None,
    normalize: bool = False,
    save: bool = False
):

    x = np.linspace(global_start, global_end, global_points)
    fig, ax = plt.subplots()

    for cfg in configs:
        func = FUNCTIONS[cfg.function]
        y = cfg.amplitude * func(cfg.frequency * x + cfg.phase)

        if cfg.noise:
            y += np.random.normal(0, cfg.noise_level, size=len(y))

        if normalize:
            y_min, y_max = y.min(), y.max()
            if y_max != y_min:
                y = (y - y_min) / (y_max - y_min)

        ax.plot(
            x,
            y,
            color=cfg.color,
            linestyle=cfg.linestyle,
            linewidth=cfg.linewidth,
            label=f"{cfg.function}, A={cfg.amplitude}, f={cfg.frequency}"
        )

    ax.set_xlim(global_start, global_end)
    if global_grid:
        ax.grid(True)

    ax.legend(loc="best")



    if title:
        ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    if save:
        filename_to_save=title or "plot.png"
        plt.savefig( filename_to_save, dpi=150)

    plt.close(fig)
    buf.seek(0)
    return buf
