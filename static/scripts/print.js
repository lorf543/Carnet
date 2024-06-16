

function imagesLoaded(element, callback) {
    const images = element.getElementsByTagName('img');
    let loadedCount = 0;
    let imageCount = images.length;
  
    if (imageCount === 0) {
      callback();
      return;
    }
  
    const checkImageLoaded = () => {
      loadedCount++;
      if (loadedCount === imageCount) {
        callback();
      }
    };
  
    for (let img of images) {
      if (img.complete) {
        checkImageLoaded();
      } else {
        img.onload = checkImageLoaded;
        img.onerror = checkImageLoaded;
        img.crossOrigin = "anonymous";
      }
    }
}
  
  function generatePDF() {
    const element = document.getElementById("pageprint");
    imagesLoaded(element, () => {
      var options = {
        margin: [-1, -4, 0, 0],
        filename: "documento.pdf",
        image: { type: "jpeg", quality: 0.9 },
        html2canvas: {
          scale: 2,
          letterRendering: true,
          useCORS: true,
          allowTaint: true,
        },
        jsPDF: {
          unit: "mm",
          format: "a4",
          orientation: "portrait",
        },
      };
  
      html2pdf().from(element).set(options).output('dataurlnewwindow');
    });
  }