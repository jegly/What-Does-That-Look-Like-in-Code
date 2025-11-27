"""
render.py - Output formatting and rendering
"""
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table
from rich import box


class OutputRenderer:
    """Renders output with rich formatting"""
    
    def __init__(self):
        self.console = Console()
    
    def render_header(self, category: str, confidence: float):
        """Render category and confidence header"""
        confidence_pct = confidence * 100
        
        # Color based on confidence
        if confidence >= 0.7:
            color = "green"
        elif confidence >= 0.4:
            color = "yellow"
        else:
            color = "red"
        
        header_text = f"[bold]{category.upper()}[/bold] (confidence: [{color}]{confidence_pct:.1f}%[/{color}])"
        self.console.print(Panel(header_text, box=box.DOUBLE))
    
    def render_ir_preview(self, ir):
        """Render compact IR preview"""
        self.console.print("\n[bold cyan]═══ INTERMEDIATE REPRESENTATION ═══[/bold cyan]")
        
        # Create a compact summary
        summary = []
        
        if ir.entities:
            summary.append(f"Entities: {', '.join([e.name for e in ir.entities])}")
        
        if ir.actions:
            summary.append(f"Actions: {', '.join([a.verb for a in ir.actions[:5]])}")
        
        if ir.assumptions:
            summary.append(f"Assumptions: {len(ir.assumptions)} defined")
        
        if ir.psychology_vars:
            summary.append(f"Psychology vars: {len(ir.psychology_vars)}")
        
        if ir.physics_vars:
            summary.append(f"Physics vars: {len(ir.physics_vars)}")
        
        summary.append(f"Uncertainty: {ir.uncertainty:.2f}")
        
        for line in summary:
            self.console.print(f"  • {line}")
        
        # Show compact JSON
        self.console.print("\n[dim]Compact JSON:[/dim]")
        json_preview = ir.to_compact_json()
        # Truncate if too long
        if len(json_preview) > 500:
            json_preview = json_preview[:500] + "\n  ... (truncated)"
        self.console.print(Panel(json_preview, box=box.MINIMAL))
    
    def render_assumptions(self, assumptions):
        """Render assumptions"""
        if assumptions:
            self.console.print("\n[bold yellow]Assumptions:[/bold yellow]")
            for assumption in assumptions:
                self.console.print(f"  • {assumption}")
    
    def render_pseudo_code(self, pseudo_code: str):
        """Render pseudo-code"""
        self.console.print("\n[bold green]═══ PSEUDO-CODE ═══[/bold green]")
        self.console.print(Panel(pseudo_code, box=box.ROUNDED))
    
    def render_python_code(self, python_code: str):
        """Render Python code with syntax highlighting"""
        self.console.print("\n[bold blue]═══ PYTHON CODE ═══[/bold blue]")
        syntax = Syntax(python_code, "python", theme="monokai", line_numbers=True)
        self.console.print(Panel(syntax, box=box.ROUNDED))
    
    def render_complete_output(self, ir, pseudo_code: str, python_code: str):
        """Render complete formatted output"""
        # Header
        self.render_header(ir.category, ir.confidence)
        
        # Assumptions
        self.render_assumptions(ir.assumptions)
        
        # IR Preview
        self.render_ir_preview(ir)
        
        # Pseudo-code
        self.render_pseudo_code(pseudo_code)
        
        # Python code
        self.render_python_code(python_code)
        
        # Footer
        self.console.print("\n[dim]═══════════════════════════════════════════[/dim]\n")


if __name__ == "__main__":
    # Test rendering
    from ir import IntermediateRepresentation
    
    ir = IntermediateRepresentation(
        raw_text="Test scenario",
        category="psychology",
        confidence=0.75,
        assumptions=["Actors have mental states", "Behavior is motivated"]
    )
    
    pseudo = "// Test pseudo-code\nIF condition THEN action"
    python = "def test():\n    print('Hello, World!')"
    
    renderer = OutputRenderer()
    renderer.render_complete_output(ir, pseudo, python)
