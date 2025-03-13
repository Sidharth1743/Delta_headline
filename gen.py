# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large")
# pip install accelerate

input_text = """Summarize the news article content:INVESTING STRATEGY IN 2025: PORTFOLIO MIX

Keep equities at 60%, fixed income at 40%

® Stick to SIPs, STPs
to avoid market
timing risks

SAIKAT NEOGI

AMID GROWING VOLATILITY and
moderate return expectations from
equities this year, experts suggest
investorsshouldlookataportfolioof
60% in equities, 30% in fixed
income and 100% in gold. Large-cap
funds are expected to outperform
small-andmid-capsin the near term
dueto premium market valuations.

In an environment of elevated
valuations, focusing on quality
growth stocks with strong funda-
mentals, sustainable earnings, and
reasonablevaluation metrics iskey.
Investors should prioritise compa-
nieswith consistent cash flows and
lowerleverage.Goldcan beaccessed
through exchange traded funds
while real estate investments may
bemade via realestate investment
trusts forflexibility.

Investorsshould sticktosystem-
atic investment plans and system-
atic transfer plans to avoid market
timing risks. Moreover, portfolio
rebalancing should be guided by a
disciplined approach rather than
market timing. In fact, investors
should set thresholds for asset allo-
cation deviations and a quarterly
reviewcan helprealign investments
with long-term goals.

Vivek Sharma, head, Investment,
Estee Advisors, says a balanced

DIVERSIFIED APPROACH

Returns in 2024

ings Lyearretums 1 lak

(in %) year ago
Gold TI 23.34) 1,23,340
Silver HE 21.12 1,21,120
ape office e.g
lyearFD (SBI) 6.8
EPF i 225
Small-cap 32.6
Misco ETE
Large-cap GE .s = 119,600

Senior Citizens
Savings Scheme

PPF

HBs2
| bas

Source: Bankbazaar.

1m Focus on quality growth stocks
with strong fundamentals,

sustainable ear
reasonable valuation metrics

1,08,200
1,07,100
periods

m Avoid the temptation to pursue
fleeting market trends or chase
the past year's outperforming
sectors

i Large-cap funds offer
stability during volatile

The road ahead
Debt

invest with moderate | Focus on gilt and
retums expectations

corporate bond funds

Dynamic bond funds
offer flexibility in a
volatile environment

Periodically rebalance portfol
to align with investment goals,
riskappetite & weather various
market conditions

approach, suchas 60% investments
in equities and 40% in debt is suit-
able for most investors this year.
“adding real estateto your portfolio
can enhance diversification,” he
says.

Similarly, Nirav Karkera, head,
Research, Fisdom, sayssectoralrota-
tion presents opportunitiesininfor
mation technology, pharma, tex-
tiles, and select consumer stocks.
“Sectorslinked to infrastructureand

FINANCIAL EXPRESS et» 07 January 2025

capex,as well as consumer discre-
tionary sectors like tourism and
automotive, show growth poten-
tial;’he adds.

Fixed-income allocation
Investors should review their
fixed-income portfolios to ensure
they align with investment goals
and risk tolerance. A diversified
approach with government bonds,
corporate debt, and other fixed-

https: //epaper. financialexpress.com/c/76551001

income instrumentsis key for sta-
bilityand predictablereturns.Grad-
ually increasing exposure to long-
term debt can help capitalise on
declining interest rates while man-
aging timing risks. A systematic
approach, such as investing in
dynamicbondfunds,helpsnavigate
volatility.

Investors should prefer a barbell
strategy—combining short-term
instruments for liquidity and high-

qualitylong-maturity debt foryield.
Sonam Srivastava, founder, Wright
Research, says gradual exposure to
Jong-maturity debt can be consid-
ered, but only if rates stabilise or
decline. “For 2025, maintaining
exposure to floating-rate bonds or
inflation-indexed securities can pro-
vide additional protection,’shesays.

‘Anil Rego, founder, Right Hori-
zons, says the liquidity easing mea-
sures bythe Reserve Bankofindia in
its December 2024 meeting signal
a possible rate cut by end of FY25,
likely leading to adeclinein bond
yields and price appreciation. “We
prefer medium-and long-maturity
bonds dueto their appealing yield
and thepotential for priceapprecia-
tion’he says.

Investors must avoid the temp-
tation to pursue fleeting market
trends or chase the past year’s out-
performing sectors. Instead, they
should focuson maintainingawell-
rounded portfoliothat can weather
variousmarket conditions.

Rebalancing demands disci-
pline,as itoften involvescounterin-
tuitive decisions, like selling your
winnersandbuying underperform-
ingassets. Sharma of EsteeAdvisors,
says investing can evoke fear in
downturns and greed duringrallies,
butrebalancing onapre-scheduled
basis—annuallyorsemi-annually—
helps you make choices rooted in
logic rather than sentiment.
“While this may not appeal to your
emotional instincts, itis often the
right choice forlong-term success,”

hesays."""

input_ids = tokenizer(input_text, return_tensors="pt").input_ids

outputs = model.generate(input_ids)
print(tokenizer.decode(outputs[0]))
