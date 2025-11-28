document.addEventListener('DOMContentLoaded', () => {
  const input = document.querySelector('#gufo-search-input');
  const lists = document.querySelectorAll('.icons-list');
  const style = document.querySelector('#gufo-search-style');
  const filterIcons = (needle) => {
    lists.forEach((list) => {
      list.querySelectorAll('.icon').forEach((item) => {
        const iconClass = Array.from(item.querySelector('.gf').classList)
          .find((cls) => cls !== 'gf') || '';
        const matches = needle && iconClass.toLowerCase().includes(needle);
        const show = needle.length < 1 ? true : !!matches;
        item.classList.toggle('icon--hidden', !show);
      });
    });
  };

  input.addEventListener('input', () => {
    const value = input.value.trim().toLowerCase();
    filterIcons(value);
  });

  let prevStyle = style.value;
  style.addEventListener('change', (event) => {
    const nextStyle = event.target.value;
    document.querySelectorAll('i.gf').forEach((icon) => {
      if(prevStyle) {
        icon.classList.remove(`${prevStyle}`);
      }
      if (nextStyle) {
        icon.classList.add(`${nextStyle}`);
      } else {
        icon.classList.remove(`${prevStyle}`);
      }
    });
    prevStyle = nextStyle;
  });
  filterIcons('');
});
