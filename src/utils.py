import logging
from typing import Dict, Optional

from bs4 import BeautifulSoup
from bs4.element import Tag
from requests import RequestException
from requests_cache.session import CachedSession

from exceptions import ParserFindTagException


def get_response(session: CachedSession, url: str) -> None:
    '''Перехватывает ошибку обращения к url.'''
    try:
        response = session.get(url)
        response.encoding = 'utf-8'
        return response
    except RequestException:
        logging.exception(
            f'Возникла ошибка при загрузке страницы {url}',
            stack_info=True
        )


def find_tag(soup: BeautifulSoup, tag: str,
             attrs: Optional[Dict[str, str]] = None) -> Tag:
    '''Перехватвает ошибку при поиске тега.'''
    searched_tag = soup.find(tag, attrs=(attrs or {}))
    if searched_tag is None:
        error_msg = f'Не найден тег {tag} {attrs}'
        logging.error(error_msg, stack_info=True)
        raise ParserFindTagException(error_msg)
    return searched_tag
