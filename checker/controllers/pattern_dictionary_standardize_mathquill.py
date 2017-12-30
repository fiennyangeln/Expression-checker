rules = [

    # Cosecant
    (r'\\operatorname\{cosec\}', '\\csc'),
    # Multiply sign indicated by circle dot
    (r'\\cdot', '*'),
    # Multiply sign indicated by cross
    (r'\\times', '*'),
    (r'·|\.','*'),
    # Degree to radian conversion
    (r'\^\{\\circ\}', '/180*\\pi'),
    # Degree to radian conversion
    (r'\\degree', '/180*\\pi'),
    # Trigonometric and logarithmic without bracket
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)([0-9]+([A-Za-z]|\\alpha|\\beta))',
     r'\\\1{\2}'),
    # Curly bracket for one-character after power sign
    (r'\^([a-zA-Z0-9])', r'^{\1}'),
    # Curly bracket for one-character after underscores sign
    (r'\_([a-zA-Z0-9])', r'_{\1}'),
    # Take back wrong conversion
    (r'\{\^\}', r'^'),  # Only cap inside curly bracket
    # Trigonometric and logarithmic with power
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\^\{(\S+)\}\\left\(([0-9A-Za-z\+\-\^\/\\\(\)'
     r'\{\}\.]+)\\right\)',
     r'\\\1^{\2}{\3}'),
    # Inverse trigonometric
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\^\{-1\}\\left\(([0-9A-Za-z\+\-\^\/\\\(\)'
     r'\{\}\.]+)\\right\)',
     r'\\\1^{-1}{\2}'),
    # Trigonometric and logarithmic
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\\left\(([0-9A-Za-z\+\-\^\/\\\(\)\{\}\.]+)'
     r'\\right\)', r'\\\1{\2}'),
    # Single trigonometric expression without power with symbol
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\^\{(\S+)\}([0-9A-Za-z]+)([\+\-\\]?)',
     r'\\\1^{\2}{\3}\4'),
    # Single trigonometric expression without symbol
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)([0-9A-Za-z]+)([\+\-\\]?)',
     r'\\\1{\2}\3'),

]
