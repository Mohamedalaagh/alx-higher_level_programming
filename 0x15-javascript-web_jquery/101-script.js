$(document).ready(() => {
  const addItemButton = $('DIV#add_item');
  const removeItemButton = $('DIV#remove_item');
  const clearListButton = $('DIV#clear_list');
  const myList = $('UL.my_list');

  if (addItemButton.length && removeItemButton.length && clearListButton.length && myList.length) {
    addItemButton.click(() => {
      myList.append('<li>Item</li>');
    });

    removeItemButton.click(() => {
      myList.find('li:last').remove();
    });

    clearListButton.click(() => {
      myList.empty();
    });
  } else {
    console.error('One or more elements not found');
  }
});
