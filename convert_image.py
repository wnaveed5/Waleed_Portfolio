import cairosvg

# Convert SVG to PNG
cairosvg.svg2png(url='images/medical-project.svg', 
                 write_to='images/medical-project.png',
                 output_width=800,  # Double the size for better quality
                 output_height=400) 