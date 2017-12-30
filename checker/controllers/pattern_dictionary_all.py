rules = [
    #+? denotes not-greedy search ref: (http://stackoverflow.com/a/1919995)
    # For Mathquill
    # Cosecant
    (r'\\operatorname\{cosec\}', '\\csc'),
    # Multiply sign indicated by circle dot
    (r'\\cdot', '*'),
    # Multiply sign indicated by cross
    (r'\\times', '*'),
    # Degree to radian conversion
    (r'\^\{\\circ\}', '/180*\\pi'),
    # Degree to radian conversion
    (r'\\degree', '/180*\\pi'),
    # Improper fraction
    (r'(\d+)\\frac\{(\d+)\}\{(\d+)\}', r'(\1+(\2)/(\3))'),
    # Move the variable/symbol after fraction inside the numerator of fraction
    (r'\\frac\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}'
     r'([A-Za-z]|\\alpha|\\beta|\\gamma|\\theta|\\lambda|\\mu|\\sigma|\\pi)(\^\d+)',
     r'\\frac{\1\3\4}{\2}'),
    # Trigonometric and logarithmic with power but without bracket
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\^([0-9A-Za-z])([0-9]*([A-Za-z]|\\alpha|'
     r'\\beta|\\gamma|\\theta|\\lambda|\\mu|\\sigma|\\pi)?)',
     r'\\\1^{\2}{\3}'),
    # Trigonometric and logarithmic with power but without bracket but contain fraction
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\^([0-9A-Za-z])\\frac\{([0-9]*([A-Za-z]|'
     r'\\alpha|\\beta|\\gamma|\\theta|\\lambda|\\mu|\\sigma|\\pi)?)\}\{([0-9]+)\}',
     r'\\\1^{\2}{\\frac{\3}{\5}}'),
    # Trigonometric and logarithmic without bracket but contain fraction
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\\frac\{([0-9]*([A-Za-z]|\\alpha|'
     r'\\beta|\\gamma|\\theta|\\lambda|\\mu|\\sigma|\\pi)?)\}\{([0-9]+)\}',
     r'\\\1{\\frac{\2}{\4}}'),
    # Trigonometric and logarithmic without bracket
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)([0-9]+([A-Za-z]|\\alpha|\\beta))',
     r'\\\1{\2}'),
    # Curly bracket for one-character after power sign
    (r'\^([a-zA-Z0-9])', r'^{(\1)}'),
    # Curly bracket for one-character after underscores sign
    (r'\_([a-zA-Z0-9])', r'_{(\1)}'),
    # Take back wrong conversion
    (r'\{\^\}', r'^'),  # Only cap inside curly bracket
    # Fraction with expression inside
    (r'\\frac\{([0-9A-Za-z\[\]\+\-\*\/\\\(\)\.\^]+)\}\{([0-9A-Za-z\[\]\+\-\*\/\\\(\)\.\^]+)\}',
     r'(\1)/(\2)'),
    # Trigonometric and logarithmic with power
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\^\{(\S+)\}\\left\(([0-9A-Za-z\+\-\^\/\\\(\)'
     r'\{\}\.]+)\\right\)',
     r'\\\1^{\2}{\3}'),
    # Inverse trigonometric
    #(r'\\(sin|cos|tan|cot|sec|csc|log|ln)\^\{-1}\\left\(([0-9A-Za-z\+\-\^\/\\\(\)'
    # r'\{\}\.]+)\\right\)',
    # r'\\\1^{\2}{\3}'),
    # Trigonometric and logarithmic
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\\left\(([0-9A-Za-z\+\-\^\/\\\(\)\{\}\.]+)'
     r'\\right\)', r'\\\1{\2}'),
    # Single trigonometric expression with power with symbol
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\^\{(\S+)\}([0-9A-Za-z]*)(\\alpha|\\beta|'
     r'\\gamma|\\lambda|\\theta|\\mu|\\sigma|\\pi)([\+\-\\]?)',
     r'\\\1^{\2}{\3\4}\5'),
    # Single trigonometric expression with symbol
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)([0-9A-Za-z]*)(\\alpha|\\beta|\\gamma|'
     r'\\lambda|\\theta|\\mu|\\sigma|\\pi)([\+\-\\]?)',
     r'\\\1{\2\3}\4'),
    # Single trigonometric expression without power with symbol
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\^\{(\S+)\}([0-9A-Za-z]+)([\+\-\\]?)',
     r'\\\1^{\2}{\3}\4'),
    # Single trigonometric expression without symbol
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)([0-9A-Za-z]+)([\+\-\\]?)',
     r'\\\1{\2}\3'),
    # Single trigonometric expression with nth root
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\\sqrt\[(\d+)\]\{(\S+)\}',
     r'\\\1{\sqrt[\2]{\3}}'),
    # Single trigonometric expression with square root
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\\sqrt\{(\S+)\}',
     r'\\\1{\sqrt{\2}}'),
    # Variable or constant as the base
    (r'(\d+|[a-zA-Z])\^\{', r'{\1}^{'),
    # Absolute function as the base
    (r'\\left\|([0-9A-Za-z\+\-\^\/\\\(\)\{\}\.]+)\\right\|\^', r'{|\1|}^'),
    # Expression inside bracket as the base
    (r'\\left\(([0-9A-Za-z\+\-\^\/\\\(\)\{\}\.]+?)\\right\)\^', r'{\1}^'),
    # Take back wrong conversion
    # Symbol
    (r'\\(p|alph|bet|gamm|thet|lambd|m|sigm)\{([a-zA-Z])\}', r'{\\\1\2}'),
    # Trigonometric operator #1
    (r'(sin|cos|tan|cot|sec|csc|log|ln)\{\^\}', r'\1^'),
    # Trigonometric operator #2
    (r'(si|co|ta|se|cs|lo|l)\{([a-zA-Z])}', r'\1\2'),
    #Integration with Fraction
    #(r'\\frac\{d([a-zA-Z]|\\alpha|\\beta|\\gamma|\\lambda|\\theta|\\mu|\\sigma)\}\{...\}',
     #r'(d\1)/(\2)'),
    # Wrong conversion for integration
    (r'\\d([a-zA-Z]|\\alpha|\\beta|\\gamma|\\lambda|\\theta|\\mu|\\sigma)',
     r'\\d\1'),
    # Bracket
    (r'\\left\(', r'('),  # left bracket
    (r'\\right\)', r')'),  # right bracket
    (r'\\left\{', r'{'),  # left bracket
    (r'\\right\}', r'}'),  # right bracket
    (r'\\left\[', r'('),  # left bracket
    (r'\\right\]', r')'),  # right bracket
    # Preprocess of plus minus symbol
    (r'\\pm', r'(pm)'),
    (r'\\mp', r'(mp)'),
    # Absolute function
    (r'\{\|([0-9A-Za-z\+\-\*\/\\\(\)\.\^\{\}]+?)\|\}', r'|\1|'),
    # Absolute function (for Mathquill)
    (r'(\\left)?\|([0-9A-Za-z\+\-\*\/\\\(\)\.\^\{\}]+?)(\\right)?\|', r'{abs(\2)}'),
    # Coefficient of a variable
    (r'(\d+\.?\d*\.?\d*|\}|\))([a-zA-Z])', r'\1*\2'),
    # Cofficient of pi (alphanumeric only)
    (r'([a-zA-Z]|\d+\.?\d*)\\pi', r'\1*\pi'),
    # Factorial
    (r'(\d+)\!', r'factorial(\1)'),
    # Fraction with simple expression
    (r'\\frac\{([0-9a-zA-Z\.\+\-]+|\\pi)\}\{([0-9a-zA-Z\.\+\-]+|\\pi)\}',
     r'(\1)/(\2)'),
    # Power without bracket at all
    (r'(\d+\.?\d*|[A-Za-z]|\\pi)\^(\d+\.?\d*|[A-Za-z]|\\pi)', r'(\1)**(\2)'),
    # Differentiation
    (r'\\frac\{d\}\{d([a-zA-Z]|\\alpha|\\beta|\\gamma|\\lambda|\\theta|\\mu|\\sigma)\}'
     r'\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}',
     r'diff(\2, \1)'),
    # Indefinite integration
    (r'\\int([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)d([a-zA-Z]|\\alpha|\\beta|\\gamma|'
     r'\\lambda|\\theta|\\mu|\\sigma)',
     r'integrate(\1, \2)'),
    # Reversing the upper bound and lower bound of definite integration if needed
    (r'\\int\^\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}\_\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}',
     r'\int_{\2}^{\1}'),
    # Definite integration parsing needs to have 2 steps in order to reduce error
    # Definite integration parsing step #1
    (r'\\int\_\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}\^\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}',
     r'\int_from{\1}_to{\2}'),
    (r'\\int\^\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}\_\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}',
     r'\int_from{\2}_to{\1}'),
    # Complex number
    (r're\^\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}', r're(\1)'),
    (r'im\^\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}', r'im(\1)'),
    # Exponent with power
    (r'\{e\}\^\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}', r'exp(\1)'),
    # Power with curly bracket in its base only
    (r'\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}\^([0-9]+|[A-Za-z])', r'(\1)**(\2)'),
    # Power with curly bracket
    (r'\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}\^\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}',
     r'(\1)**(\2)'),
    # Nested power
    (r'\)\^(\d+)', r')*\1'),
    # n-th root
    (r'\\sqrt\[(\d+)\]\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}', r'root(\2, \1)'),
    # Square root
    (r'\\sqrt\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}', r'sqrt(\1)'),
    # Fraction with expression inside
    (r'\\frac\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}',
     r'(\1)/(\2)'),
    # Inverse trigonometric from sin/cos/tan to power of -1
    (r'\\(sin|cos|tan)\^\{\-1\}\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}', r'arc\1(\2)'),
    # Trigonometric and logarithmic with power
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\^\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}'
     r'\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}',
     r'\1(\3)**(\2)'),
    # Trigonometric and logarithmic
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}',
     r'\1(\2)'),
    # Inverse trigonometric
    (r'\\arc(sin|cos|tan)\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}', r'arc\1(\2)'),
    # Power to handle mathematical function in the form e.g. (ln x)^2
    (r'\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}\^\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}',
     r'(\1)**(\2)'),
    # Fraction with expression inside
    (r'\\frac\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}',
     r'(\1)/(\2)'),
    # Sqrt and nth root must be done again in order to handle
    # sqrt or nth root of trigonometric function
    # n-th root
    (r'\\sqrt\[(\d+)\]\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}', r'root(\2, \1)'),
    # Square root
    (r'\\sqrt\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}', r'sqrt(\1)'),
    # Exponent to handle complex number
    (r'\{e\}\^\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}', r'exp(\1)'),
    # Complex number as coefficient
    (r'i\(', r'i*('),
    # Cofficient of pi
    (r'\)\\pi', r')*\pi'),
    # Coefficient of inverse trigonometric function
    (r'([0-9a-zA-Z]+|\\pi|\))(arcsin|arccos|arctan)',
     r'\1*\2'),
    # Coefficient of trigonometric and logarithmic function
    (r'([0-9a-zA-Z]+|\\pi|\))(sin|cos|tan|cot|sec|csc|log|ln)', r'\1*\2'),
    # Convert back to inverse trigonometric function
    (r'arc\*(sin|cos|tan)', r'arc\1'),
    # Coefficient of expression inside bracket
    (r'(\d+|[a-zA-Z]|\\pi)\(',  r'\1*('),
    # Coefficient of exponent
    (r'([0-9a-zA-Z]+|\\pi|\)+)exp',  r'\1*exp'),
    # Coefficient of square root
    (r'([0-9a-zA-Z]+|\\pi|\)+)sqrt', r'\1*sqrt'),
    # Coefficient of nth root
    (r'([0-9a-zA-Z]+|\\pi|\)+)root', r'\1*root'),
    # Coefficient of a symbol
    (r'(\)|\d+)(\\[a-zA-Z]+)', r'\1*\2'),
    # pi as a coefficient of expression without bracket
    (r'\\pi(\\|\()', r'\pi*\1'),
    # pi as a coefficient of expression in bracket
    (r'\\pi\(', r'\pi*('),
    # 2 consecutive parentheses
    (r'\)\(', r')*('),
    # Digits after parentheses
    (r'\)(\d+)', r')*\1'),
    # Trigonometry, logarithm, and inverse logarithm (for Mathquill)
    # Inverse trigonometric
    (r'\\(sin|cos|tan)\^\{\-1}([0-9A-Za-z\+\-\^\/\\\(\)\{\}\.]+)', r'arc\1(\2)'),
    # Trigonometric and logarithmic with power
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\^\{(\S+)\}([0-9A-Za-z\+\-\^\/\\\(\)\{\}\.]+)',
     r'\1(\3)**(\2)'),
    # Trigonometric and logarithmic without power
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)([0-9A-Za-z\+\-\^\/\\\(\)\{\}\.]+)',
     r'\1(\2)'),

    # * before d_ in definite integration
    (r'\\int(\S+)\*d', r'\int\1d'),
    # Definite integration parsing step #2
    (r'\\int_from\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}_to\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}'
     r'([0-9A-Za-z\+\-\*\/\\\(\)\{\}\.\^]+)d([a-zA-Z]|\\alpha|\\beta|\\gamma|\\lambda|'
     r'\\theta|\\mu|\\sigma)',
     r'integrate(\3, (\4, \1, \2))'),
    # pi as a coefficient of integration
    (r'\\piintegrate', r'\pi*integrate'),
    # backup for trigonometric, logarithmic, exponent function which was added
    # with '*'
    (r'(sin|cos|tan|cot|sec|csc|log|ln|exp|sqrt|root|integrate|re|im|factorial|abs)\*',
     r'\1'),
    # Symbol
    (r'\\alpha', r'a'),
    (r'\\beta', r'b'),
    (r'\\gamma', r'c'),
    (r'\\theta', r't'),
    (r'\\lambda', r'l'),
    (r'\\mu', r'm'),
    (r'\\sigma', r's'),
    # Two consecutive character (variables)
    (r'([a-zA-Z])([a-zA-Z])', r'\1*\2'),
    # Take back wrong conversion
    (r'a\*r\*c\*s\*i\*n', r'asin'),
    (r'a\*r\*c\*c\*o\*s', r'acos'),
    (r'a\*r\*c\*t\*a\*n', r'atan'),
    (r's\*i\*n', r'sin'),
    (r'c\*o\*s', r'cos'),
    (r't\*a\*n', r'tan'),
    (r'c\*o\*t', r'cot'),
    (r's\*e\*c', r'sec'),
    (r'c\*s\*c', r'csc'),
    (r'l\*o\*g', r'log'),
    (r'l\*n', r'ln'),
    (r'e\*x\*p', r'exp'),
    (r's\*q\*r\*t', r'sqrt'),
    (r'r\*o\*o\*t', r'root'),
    (r'i\*n\*t\*e\*g\*r\*a\*t\*e', r'integrate'),
    (r'r\*e', r're'),
    (r'i\*m', r'im'),
    (r'f\*a\*c\*t\*o\*r\*i\*a\*l', r'factorial'),
    (r'f\*r\*a\*c', r'frac'),
    (r'a\*b\*s', r'abs'),
    (r'p\*i', r'pi'),
    (r'p\*m', r'pm'),
    (r'm\*p', r'mp'),
    (r'rexp', r'r*exp'),
    #Fraction with simple expression one more time
    (r'\\frac\{([0-9A-Za-z\[\]\+\-\*\/\\\(\)\.\^]+)\}\{([0-9A-Za-z\[\]\+\-\*\/\\\(\)\.\^]+)\}',
    r'(\1)/(\2)'),

    # pi
    (r'\\pi', r'pi'),
    # Capital letter (which SymPy cannot work with)
    (r'N', r'n'),
    # Postprocess of plus minus symbol
    (r'\*?\(pm\)\*?', r'pm'),
    (r'\*?\(mp\)\*?', r'mp'),
    # Unnecessary brackets
    (r'\{|\[', r'('),
    (r'\}|\]', r')'),
    # 2 consecutive parentheses, sometimes needed at the end
    (r'\)\(', r')*('),


]
