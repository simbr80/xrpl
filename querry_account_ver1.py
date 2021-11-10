from xrpl.clients import JsonRpcClient
from xrpl.models.requests.account_lines import AccountLines
from time import perf_counter

t_start = perf_counter()

JSON_RPC_URL = "https://s2.ripple.com:51234/"
client = JsonRpcClient(JSON_RPC_URL)

all_lines = []
test = True
marker = None

while test == True:
# Look up info about account lines

    acct_info = AccountLines(
        account='rLqUC2eCPohYvJCEBJ77eCCqVL2uEiczjA',
        marker=marker,
        limit=400
    )
    response = client.request(acct_info)
    result = response.result

    part_lines = result["lines"]
    if not "marker" in result.keys():
        test = False
        all_lines.extend(part_lines)
    else:
        marker = result["marker"]
        all_lines.extend(part_lines)
        print(marker)


for i in all_lines:
    i['balance'] = float(i['balance'])

all_lines_sorted = sorted(all_lines, key=lambda d: d['balance'])

t_stop = perf_counter()
print("Elapsed time:", t_stop, t_start)
print(f"Elapsed time during the whole program in seconds: {t_stop - t_start}")