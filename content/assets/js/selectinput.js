window.addEventListener('load', function (e) {
   // selects hidden selectbox, label, custom dropdown
   let selects =  document.querySelectorAll('.select-field');

   for(let node of selects){
      if (!node.querySelectorAll('option').length) {
        continue;
      }
      //custom dropdown
      let customSelect = node.lastElementChild
      //selects text element for dropdown, set the initial value same as in hidden select box of form.
      let selectValue = customSelect.firstElementChild.firstElementChild
      let select = node.firstElementChild
      let text = select.options[select.selectedIndex].text;
      selectValue.textContent = text;

      let dropdownsItems = customSelect.lastElementChild.querySelectorAll('.dropdown-item');
      dropdownsItems.forEach( item => {
         if(item.textContent === text) {
            item.classList.add('option-selected')
         } else {
            item.classList.remove('option-selected')
         }
         item.addEventListener('click',()=>{
            selectValue.textContent = item.textContent
            // assign select item id to hidden select box.
            select.value = item.classList[0];
            let previousItem = customSelect.lastElementChild.querySelector('.option-selected');
            previousItem.classList.remove('option-selected')
            item.classList.add('option-selected')
         })
      })
   }
})