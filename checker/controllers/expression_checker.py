from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from . import answer_transformer
"""
Compare 2 Latex expressions and return the correctness of the answer.
In between, there is a need to transform the expression in Latex syntax into
ASCII syntax.
"""


def check(x, y):
    print(x)
    print(y)
    x_ascii = answer_transformer.transform_latex_to_sympy(x)
    y_ascii = answer_transformer.transform_latex_to_sympy(y)
    result = evaluate_answer_in_ascii(x_ascii, y_ascii)
    return result


"""
Evaluates the transformed Latex and returns the correctness of the answer.
"""


def evaluate_answer_in_ascii(x, y):
    if x and y:
        try:
            # Check the existence of +- sign or -+ sign
            xPlusMinus = (x.count("pm") + x.count("mp")) > 0
            yPlusMinus = (y.count("pm") + y.count("mp")) > 0
            equal_no_of_pm = (x.count("pm") + x.count("mp")
                              ) == (y.count("pm") + y.count("mp"))

            if (xPlusMinus or yPlusMinus) and not equal_no_of_pm:
                # Different number of +- and -+ between 2 expressions, then
                # automatically wrong
                return False
            if xPlusMinus and yPlusMinus and equal_no_of_pm:
                # Handle +-
                # +- needs to be handled manually since Sympy cannot handle +-
                # nor - +
                # Split the expression into 2 parts, one contains + whereas the
                # other contains -
                x1 = parse_expr(x.replace('pm', '+').replace('mp', '-'))
                x2 = parse_expr(x.replace('pm', '-').replace('mp', '+'))
                y1 = parse_expr(y.replace('pm', '+').replace('mp', '-'))
                y2 = parse_expr(y.replace('pm', '-').replace('mp', '+'))
                # Check individually
                z1 = simplify(x1 - y1)
                z2 = simplify(x2 - y2)
                # Both must be correct
                return (z1 == 0 and z2 == 0)
            elif not xPlusMinus and not yPlusMinus:
                # No +- nor -+ sign found, so handle the expression normally
                x = parse_expr(x)
                y = parse_expr(y)
                z = simplify(x - y)
                #print(x)
                return(z == 0)
        except:
            print(x)
            return False
    else:
        # No answer specified
        return False

def test_expression():
    test_datas = [
        ["0", True],
        ["5\\times3", True],
        ["5\\cdot3", True],
        ["n \\pi \\pm \\frac{1}{6} \\pi", True],
        ["\\frac{1}{2}x^2 + \\frac{1}{12}x^4", True],
        ["\\frac{0.015}{\\pi}", True],
        ["1.05x", True],
        ["\\frac{40 \\pi r^4}{a}", True],
        ["\\frac{2a}{5}", True],
        ["\\frac{1}{x+1}+\\frac{1}{x+2}-\\frac{2}{x+3}", True],
        ["\\frac{1}{2} \\tan{x}", True],
        ["\\frac{x^2}{3} e^{3x} - \\frac{2x}{9} e^{3x} + \\frac{2}{27} e^{3x}", True],
        ["\\frac{x-y}{x-2y}", True],
        ["2\\pi - \\alpha", True],
        ["\\frac{5}{3} \\pi", True],
        ["e^{-x}(A \\sin{2x} + B \\cos{2x})+(1+4x)", True],
        ["3 \\pm 2\\sqrt{2} \\mp 2\\sqrt{2i}", True],
        ["-2e^x(\\cos{x} + \\sin{x})", True],
        ["1+x-\\frac{1}{3}x^3", True],
        ["\\sqrt{6}", True],
        ["\\frac{1}{2}(e^{2.56} -1)", True],
        ["\\frac{2}{1-x}+\\frac{1}{{(1-x)}^2}+\\frac{1}{2+x}", True],
        ["\\frac{1}{50}(139i+85j+2k)", True],
        #["180n^{\\circ}-45n^{\\circ}", False],
        ["-(\\frac{3x^2 + y}{x+6y^2})", True],
        ["\\frac{1}{2} \\ln{(x^2+2x+5)} + \\frac{1}{2} \\tan^{-1}{\\frac{x+1}{2}}", True],
        ["3 \\sin^{2}{\\theta}", True],
        ["\\pi", True],
        ["(\\pi^2)*(\\frac{\\pi^2}{3} + \\frac{21}{2})", True],
        ["\\frac{1}{9}{(3-x)}^2", True],
        ["2i", True],
        ["-2-4i", True],
        ["i\\frac{1}{2} \\cot{(\\frac{1}{2}\\theta)}-\\frac{1}{2}", True],
        ["2 \\tan{(- 3{x}^{2} + c)}", True],
        ["2x+y-1", True],
        ["n\\pi + {(-1)}^n(-0.340)", True],
        ["\\frac{9}{2} \\sin{\\theta} - \\frac{1}{2}\\theta", True],
        ["1+14y+91y^2+364y^3", True],
        ["(e^x +2)-2 \\ln{(e^x +2)}", True],
        ["- \\frac{1}{\\sqrt{1-x^2}}", True],
        ["\\frac{1}{2}(3^n-1)+n(n+1)", True],
        ["\\frac{c\\sin{\\alpha}}{\\sin{\\theta}}", True],
        ["\\frac{b\\sin{\\alpha}}{\\sin{(\\pi-\\theta)}}", True],
        ["\\frac{1}{\\sqrt{2}+1}", True],
        ["\\frac{1}{2+\\sqrt{3}}", True],
        ["\\frac{1}{2}(1-\\cos{2x})", True],
        ["6 + 5 \\sin{(2x+\\alpha)}", True],
        ["\\sin{x} - x \\cos{x}", True],
        ["(\\frac{1}{\\sqrt{2}} - (\\frac{1}{4*\\sqrt{2}}*\\pi))*(\\ln{\\sqrt{2} + 1})-(\\frac{1}{2}*\\ln{2})+(\\frac{1}{32} *(\\pi^2))", True],
        ["\\frac{3}{32}(4x-x^2)", True],
        ["2R\\cos{\\frac{1}{2}(\\beta-\\alpha)}", True],
        ["\\frac{1}{2}(\\alpha+\\beta)", True],
        ["{(2x+y)}^2+(2x+y)", True],
        ["\\frac{1}{1-\\sin{x}}", True],
        ["x-\\frac{1}{2}x^2", True],
        ["\\pi\\int_{1}^{3}{{(x^3 +1)}^{\\frac{1}{2}}}", True],
        ["\\frac{1}{2}x + \\frac{1}{12} \\sin{6x}", True],
        ["\\frac{1}{2}\\tan{2x}-x", True],
        ["4 \\cos{\\theta}", True],
        ["5*\\ln{5} -4", True],
        ["\\sqrt{\\frac{2}{3}}", True],
        ["1-x+x^2-\\frac{11}{3}x^3", True],
        ["\\frac{1}{3}a+\\frac{1}{3}b+\\frac{1}{3}c", True],
        ["N", True],
        ["\\mu", True],
        ["{\\sigma}^{2}", True],
        ["(\\frac{1}{2}*\\sqrt{3})+\\frac{1}{6}", True],
        ["\\tan{(x^2 + \\frac{\\pi}{4})}", True],
        #["\\frac{2}{(1+x^2)^3} + \\frac{3}{(1+x^2)^2}", True],
        ["\\frac{11}{12}*\\pi", True],
        ["-1-i", True],
        ["1-\\sqrt{3}i", True],
        ["-1-\\sqrt{3}", True],
        ["2\\sqrt{2}+i[2+2\\sqrt{2}]", True],
        ["-i+4j+2k", True],
        ["3i-j-k", True],
        ["1+2x+3x^2", True],
        ["e^{a}(x-a+1)", True],
        ["ex", True],
        ["\\frac{3*\\pi}{4}", True],
        ["e-2", True],
        ["-\\sin^{-1} {\\frac{1}{x}}", True],
        ["\\frac{\\pi}{2}", True],
        ["\\frac{1}{a}x", True],
        ["\\frac{1}{a^2}x^2", True],
        ["\\frac{2}{3}a", True],
        ["\\frac{1}{18}a^2", True],
        ["\\frac{1}{\\sqrt{2}}a", True],
        ["2-i", True],
        ["2*\\sqrt{2}", True],
        ["\\frac{3}{4}*\\pi", True],
        ["x^2 + \\frac{C}{x^3}", True],
        ["\\frac{2}{3}i-\\frac{2}{3}j-\\frac{1}{3}k", True],
        ["|b|^2+|c|^2 - 2bc", True],
        #["AC^2+AB^2-2(AC)(AB)\\cos{\\angle BAC}", False],
        ["\\frac{1}{2}(2^N - 1)+\\frac{3}{2}N(N+1)", True],
        ["-\\frac{1}{\\sqrt{2}}", True],
        ["2xe^{x^2}", True],
        ["\\frac{1}{2} e^{x^2}", True],
        ["\\frac{\\sin^{-1} {x}}{\\sqrt{1-x^2}}", True],
        ["x - \\frac{1}{2(x+1)} + \\frac{3}{2(x-1)}", True],
        ["2\\cos{2\\theta}\\cos{\\theta}", True],
        ["-\\frac{1}{4}-\\frac{\\sqrt{5}}{4}", True],
        ["\\ln{2}", True],
        ["(\\frac{4}{3}*(\\pi^2))-(\\sqrt{3}*\\pi)", True],
        ["1-2x+7x^2", True],
        ["-\\frac{1}{4}", True],
        ["\\pi-\\theta", True],
        ["\\frac{1}{2}\\pi-\\theta", True],
        ["\\sqrt{\\frac{1}{4}x^2-1}+\\frac{1}{2}x", True],
        ["\\frac{3}{8}{(x-1)}^2", True],
        ["2n\\pi\\pm\\frac{2}{3}\\pi", True],
        ["\\frac{2-x}{x^2+1}+\\frac{1}{x+2}", True],
        ["\\frac{5}{2}-\\frac{5}{4}x-\\frac{15}{8}x^2", True],
        ["\\frac{\\sqrt{2*\\pi}}{32}*((\\pi^2) + (8*\\pi) - 32)", True],
        ["\\frac{4}{x(8-7x)}", True],
        ["\\frac{1}{4} x^4 x - \\frac{x^4}{16}", True],
        ["\\frac{1}{4} x^4 {(\\ln{x})}^2 - \\frac{1}{8} x^4 \\ln{x} + \\frac{1}{32} x^4", True],
        ["x - \\frac{1}{2}x^2 + \\frac{1}{6}x^3", True],
        ["n\\pi +{(-1)}^{n}(-\\frac{1}{6}\\pi)", True],
        ["\\frac{3x}{6-x}", True],
        ["36-(18*\\ln{3})", True],
        ["3-\\frac{35}{6}x", True],
        ["1+2i", True],
        ["\\frac{1}{2} + x + ce^{2x}", True],
        ["\\sqrt{\\frac{2}{1+2x}}", True],
        ["1-\\frac{1}{3}x^2 + \\frac{2}{9}x^4", True],
        ["\\frac{1}{2x+cx^2}", True],
        ["25{\\lambda}^{4} + 30{\\lambda}^{3}", True],
        ["-9{\\lambda}^{2}", True],
        ["3\\lambda", True],
        ["3\\lambda\\pm\\sqrt{9{\\lambda}^{2}+x}", True],
        ["\\frac{1}{3} \\ln{|x^3+1|}", True],
        ["\\ln{|x+1|}", True],
        ["\\frac{2}{\\sqrt{3}} \\tan^{-1}{\\left(\\frac{2x-1}{\\sqrt{-3}}\\right)}", True],
        ["\\frac{1}{2} \\ln{|x+1|} - \\frac{1}{6}\\ln{|x^3+1|} + \\frac{1}{\\sqrt{3}}\\tan^{-1}{\\frac{2x-1}{\\sqrt{3}}}", True],
        ["1\\pm2i", True],
        ["\\frac{2}{3}a", True],
        ["\\frac{n(n-1)(n-2)}{(n+3)(n+2)(n+1)}", True],
        ["\\frac{9n(n-1)}{(n+3)(n+2)(n+1)}", True],
        ["\\frac{18n(n-1)}{(n+3)(n+2)(n+1)}", True],
        ["\\frac{6(n-1)(n-2)}{(n+3)(n+2)(n+1)}", True],
        ["\\frac{9}{(n+3)}", True],
        ["\\frac{3n}{n+3}", True],
        ["\\frac{9n^2}{{(n+3)}^2(n+2)}", True],
        ["\\frac{9n^2}{\\left(n+3\\right)^2(n+2)}", True],
        ["\\frac{15}{x} + 3", True],
        ["f^2", True],
        ["\\frac{1}{12}*\\pi", True],
        ["\\frac{1}{3}n\\pi + {(-1)}^{n} (-0.283)", True],
        ["n^2(2n^2-1)", True],
        ["\\frac{\\sin^{-1}{x} + c}{\\sqrt{1-x^2}}", True],
        ["\\frac{4}{3*\\sqrt{3}}*\\pi", True],
        ["-\\frac{1}{prq}", True],
        ["i+(5\\lambda -2)j+5(1-\\lambda)k", True],
        ["(10-12\\mu)i+(1+3\\mu)j+(2+3\\mu)k", True],
        ["\\frac{15}{\\sqrt{2}}", True],
        ["\\frac{1}{12}x(8-x)", True],
        ["\\frac{2}{3}(1+2e^{-\\frac{3}{4}t})", True],
        ["\\frac{1}{3}(4i+2j+5k)", True],
        ["re^{-i\\theta}", True],
        ["2e^{\\pm i\\frac{\\pi}{2}}", True],
        ["2e^{\\pm i\\frac{5\\pi}{6}}", True],
        ["(z+4)(z^2-2\\sqrt{3z} + 4)(z^2+2\\sqrt{3z}+4)", True],
        ["1+ nx + \\frac{n(n-1)}{2!}x^2+\\frac{n(n-1)(n-2)}{3!}x^3", True],
        ["-\\frac{\\sqrt{2}}{2}", True],
        ["-\\frac{1}{2-x} + \\frac{x+1}{1+x^2}", True],
        ["\\frac{1}{2} + \\frac{3}{4} - \\frac{9}{8}x^2", True],
        ["\\frac{1}{4}*(-1+\\sqrt{5})", True],
        ["\\frac{1}{4}*(-1-\\sqrt{5})", True],
        ["(3*\\ln{2}) + (\\frac{1}{3}*\\pi)", True],
        ["(\\frac{3}{2}*(4*\\ln{5})) - (3*\\ln{2})", True],
        ["2x \\cos{x^2}", True],
        ["\\frac{1}{2}(x^2 \\sin{x^2} + \\cos{x^2})", True],
        ["1 - \\frac{1}{{(N+1)}^2}", True],
        ["\\left( x\\frac{dy}{dx}+y \\right)", True],
        ["\\frac{1}{{(xy)}^{2}+1}", True],
        ["\\frac{1}{{x}^{2}+1}", True],
        ["-\\sin{\\ln{\\left(1+x\\right)}}\\left(\\frac{1}{1+x}\\right)", True],
        ["-\\cos{\\ln{\\left(1+x\\right)}}", True],
        ["{(1+x)}^2", True],
        ["\\left(1+x\\right)^2", True],
        ["3(1+x)", True],
        ["1-\\frac{1}{2}x^2+\\frac{1}{2}x^3", True],
        ["\\frac{[(x^2 + 32)-(x^2)]{(x^2 + 32)}^{-\\frac{1}{2}}}{(x^2 + 32)}", True],
        ["-2\\sin{t}\\cos{t}", True],
        ["3\\sin^{2}{t}\\cos{t}", True],
        ["-\\frac{3}{2}\\sin{t}", True],
        ["-\\frac{3}{2}\\sin{\\theta}", True],
        ["-\\frac{3}{2}\\sin{\\theta}(x-\\cos^{2}{\\theta})+\\sin^{3}{\\theta}", True],
        ["\\frac{3}{2}\\sin{\\theta}\\cos^{2}{\\theta}+\\sin^{3}{\\theta}", True],
        ["\\frac{du}{\\cos{t}}", True],
        ["", False],
    ]
    counter = 0
    error_counter = 0
    error_data = []
    for test_data in test_datas:
        if check(test_data[0], test_data[0]) != test_data[1]:
            print(test_data[0] + " generates error.")
            error_data.append(test_data[0])
            error_counter = error_counter + 1
        counter = counter + 1
    print ("Total test cases: " + str(counter))
    print ("Total error: " + str(error_counter))
    success_rate = (counter*1.0 - error_counter*1.0) / counter*1.0 * 100
    print ("Success rate: " + str(success_rate) + "%")
    return error_data

def test_expression(test_datas):
    counter = 0
    error_counter = 0
    error_data = []
    for test_data in test_datas:
        if check(test_data[0], test_data[0]) != test_data[1]:
            print(test_data[0] + " generates error.")
            error_data.append(test_data[0])
            error_counter = error_counter + 1
        counter = counter + 1
    print(error_data)
    print ("Total test cases: " + str(counter))
    print ("Total error: " + str(error_counter))
    success_rate = (counter*1.0 - error_counter*1.0) / counter*1.0 * 100
    print ("Success rate: " + str(success_rate) + "%")
    return error_data
