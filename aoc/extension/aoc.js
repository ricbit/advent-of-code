const preElements = document.querySelectorAll('pre');
const codeElements = document.querySelectorAll('code:not(pre code)');

// Convert NodeLists to Arrays and merge them
const allElements = Array.from(preElements).concat(Array.from(codeElements));

// Sort allElements based on their position in the document
allElements.sort((a, b) => {
    if (a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING) {
        return -1;
    } else {
        return 1;
    }
});

// Iterate over the merged and sorted array
allElements.forEach((elem, index) => {
    let newElement = document.createElement('span');
    newElement.style.color = 'lightblue'; // Set the color to light blue

    if (elem.tagName.toLowerCase() === 'pre') {
        // For <pre> elements
        newElement.innerHTML = `SAMPLE[${index + 1}]<BR>`;
        elem.prepend(newElement); // Prepend the new element
    } else if (elem.tagName.toLowerCase() === 'code') {
        // For <code> elements
        newElement.textContent = ` [[${index + 1}]]`;
        elem.parentNode.insertBefore(newElement, elem.nextSibling);
    }
  
});


// Scroll to the bottom of the page
//window.scrollTo(0, document.body.scrollHeight);

