$(document).ready(function() {
    $('input[type=radio][name=role]').change(function() {
        if (this.value === 'seller') {
            $('.company-name').show();
            $('#hiddenRole').val('seller');
        } else {
            $('.company-name').hide();
            $('#hiddenRole').val('buyer');
        }
    });
});
