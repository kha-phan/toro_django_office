window.addEventListener('DOMContentLoaded', () => {
    const tabLinkElems = document.querySelectorAll('.tab-link');

    if (!new URL(document.location).searchParams.get('tab') && tabLinkElems[0]) {
        setTabParam(tabLinkElems[0].textContent);
    }

    tabLinkElems.forEach(el => el.addEventListener('click', e => setTabParam(el.textContent)));
});

function setTabParam(value) {
    const url = new URL(document.location);
    url.searchParams.set('tab', value);
    history.replaceState(history.state, '', url.toString());
}
