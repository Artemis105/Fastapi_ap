
from fastapi import APIRouter, Query
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional
import matplotlib
from plot_service import generate_function_plot


matplotlib.use("Agg")

class FunctionType(str, Enum):
    sin = "sin"
    cos = "cos"
    square = "square"
    triangle = "triangle"
    sawtooth = "sawtooth"


class LineStyle(str, Enum):
    solid = "solid"
    dashed = "dashed"
    dotted = "dotted"

class ColorStyle(str, Enum):
    blue = "blue"
    red = "red"
    green = "green"
    black = "black"
    pink= "pink"


class PlotConfig(BaseModel):
    function: FunctionType
    color: ColorStyle = ColorStyle.blue
    linestyle: LineStyle = LineStyle.solid
    amplitude: float = 1.0
    frequency: float = 1.0
    phase: float = 0.0
    linewidth: float = 1.5
    noise: bool = False
    noise_level: float = 0.1

router = APIRouter(prefix="/plot", tags=["plots"])

@router.post("/function")
def plot_function_endpoint(
    configs: List[PlotConfig],
    start: float = Query(0),
    end: float = Query(10),
    points: int = Query(300, ge=10, le=1000, description="Number of points"),
    grid: bool = Query(True),
    normalize: bool = Query(False, description="Normalize all signals"),
    save: bool = Query(False, description="Save plot to file"),
    title: Optional[str] = Query(None, description="Plot title"),
    xlabel: Optional[str] = Query(None, description="X-axis label"),
    ylabel: Optional[str] = Query(None, description="Y-axis label"),
):
    buf = generate_function_plot(start, end, points, grid, configs, title, xlabel, ylabel,normalize=normalize,
        save=save)
    return StreamingResponse(buf, media_type="image/png")