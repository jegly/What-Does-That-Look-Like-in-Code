#!/usr/bin/env python3
"""
main.py - CLI for "What Does That Look Like in Code" (WDLIC)
Converts natural language scenarios into pseudo-code and executable code
"""
import click
from parser import TextParser
from router import CategoryRouter
from ir import IRBuilder
from codegen import get_registry
from render import OutputRenderer
import sys


@click.command()
@click.argument('text', required=False)
@click.option('--format', 'output_format',
              type=click.Choice(['pseudo', 'python', 'all'], case_sensitive=False),
              default='all',
              help='Output format: pseudo-code, python, or both')
@click.option('--category',
              type=click.Choice(['auto', 'psych', 'psychology', 'physics', 'social', 
                               'math', 'mathematics', 'ui', 'business', 'game', 
                               'rules', 'opt', 'optimization'], case_sensitive=False),
              default='auto',
              help='Force a specific category (default: auto-detect)')
@click.option('--detail',
              type=click.Choice(['low', 'med', 'high'], case_sensitive=False),
              default='med',
              help='Level of detail in generated code')
@click.option('--seed', type=int, default=None,
              help='Random seed for reproducibility')
@click.option('--no-color', is_flag=True,
              help='Disable colored output')
def main(text, output_format, category, detail, seed, no_color):
    """
    WDLIC - What Does That Look Like in Code
    
    Convert natural language descriptions into pseudo-code and executable code.
    
    Examples:
    
      wdlic "3 Implies Balance"
      
      wdlic "Calculate trajectory of a ball at 20 m/s at 45 degrees" --format python
      
      wdlic "Optimize profit given cost constraints" --category optimization
    """
    
    # Handle interactive mode if no text provided
    if not text:
        click.echo("WDLIC - What Does That Look Like in Code")
        click.echo("Enter your scenario (or 'quit' to exit):\n")
        text = click.prompt("", type=str)
        if text.lower() in ['quit', 'exit', 'q']:
            sys.exit(0)
    
    # Set random seed if provided
    if seed is not None:
        import random
        import numpy as np
        random.seed(seed)
        np.random.seed(seed)
    
    # Initialize components
    parser = TextParser()
    router = CategoryRouter()
    ir_builder = IRBuilder()
    generator_registry = get_registry()
    renderer = OutputRenderer()
    
    try:
        # Parse input text
        features = parser.parse(text)
        
        # Route to category
        if category == 'auto':
            category_score = router.get_primary_category(features)
        else:
            # Manual category override
            from router import CategoryScore
            # Normalize category name
            category_map = {
                'psych': 'psychology',
                'math': 'mathematics',
                'opt': 'optimization'
            }
            category_name = category_map.get(category, category)
            category_score = CategoryScore(name=category_name, confidence=1.0, signals=[])
        
        # Build IR
        ir = ir_builder.build(features, category_score)
        
        # Generate code
        pseudo_code = None
        python_code = None
        
        if output_format in ['pseudo', 'all']:
            pseudo_code = generator_registry.generate_pseudo(ir)
        
        if output_format in ['python', 'all']:
            python_code = generator_registry.generate_python(ir)
        
        # Render output
        if output_format == 'pseudo':
            renderer.render_header(ir.category, ir.confidence)
            renderer.render_assumptions(ir.assumptions)
            renderer.render_pseudo_code(pseudo_code)
        elif output_format == 'python':
            renderer.render_header(ir.category, ir.confidence)
            renderer.render_python_code(python_code)
        else:  # all
            renderer.render_complete_output(ir, pseudo_code, python_code)
        
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        if '--debug' in sys.argv:
            raise
        sys.exit(1)


if __name__ == '__main__':
    main()
