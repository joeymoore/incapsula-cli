from Utils.executeRest import execute
import Utils.log
from Accounts.sub_account import SubAccount
from Utils.incapError import IncapError

logger = Utils.log.setup_custom_logger(__name__)


def r_subaccount(args):
    output = 'Get sub accounts!'
    logger.debug(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "account_id": args.account_id,
        "page_size": args.page_size,
        "page_num": args.page_num
    }
    result = read(param)

    if result.get('res') != 0:
        err = IncapError(result)
        err.log()
    else:
        for accounts in result['resultList']:
            account = SubAccount(accounts)
            account.log()


def read(params):
    resturl = '/api/prov/v1/accounts/listSubAccounts'
    if params:
            return execute(resturl, params)
    else:
        logger.error('No parameters where passed in.')