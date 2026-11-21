from dataclasses import dataclass, field


@dataclass
class MacroBreakdown:
    calories_kcal: float = 0.0
    protein_g: float = 0.0
    carbs_g: float = 0.0
    fiber_g: float = 0.0
    fat_g: float = 0.0


@dataclass
class DetectedItem:
    name: str
    estimated_grams: float
    confidence: float = 0.0
    nutrition_source: str = "placeholder"
    macros: MacroBreakdown = field(default_factory=MacroBreakdown)


@dataclass
class MealAnalysis:
    meal_id: str
    captured_at: str
    image_path: str
    items: list[DetectedItem] = field(default_factory=list)
    total_macros: MacroBreakdown = field(default_factory=MacroBreakdown)
    notes: str = ""
