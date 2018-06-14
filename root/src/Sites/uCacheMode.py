from Utils.executeRest import execute
import Utils.log
from Utils.incapError import IncapError

logger = Utils.log.setup_custom_logger(__name__)


def u_cachemode(args):
    output = 'Update cache setting on {0} to be {1}.'. format(args.site_id, args.cache_mode)
    logger.debug(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "site_id": args.site_id,
        "cache_mode": args.cache_mode,
        "dynamic_cache_duration": args.dynamic_cache_duration,
        "aggressive_cache_duration": args.aggressive_cache_duration
    }
    result = update(param)

    if result.get('res') != 0:
        err = IncapError(result)
        err.log()
    else:
        logger.debug('Result Message: %s' % (result.get('res_message')))


def update(params):
    resturl = '/api/prov/v1/sites/performance/cache-mode'
    if params:
        if "site_id" in params and "cache_mode" in params:
            return execute(resturl, params)
        else:
            logger.error('No site ID or cache mode parameter has been passed in.')
    else:
        logger.error('No parameters where applied.')