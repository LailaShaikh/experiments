<?php
$field_name = $_POST['name'];
$field_email = $_POST['email'];
$field_phone = $_POST['phone'];
$field_message = $_POST['message'];
$mail_to = 'nextdoor.overseas@gmail.com';
$subject = 'Enquiry message from a visitor '.$field_name;
$body_message = 'From: '.$field_name."\n";
$body_message .= 'E-mail: '.$field_email."\n";
$body_message .= 'Phone: '.$field_phone."\n";
$body_message .= 'Message: '.$field_message;
$headers = 'From: '.$field_email."\r\n";
$headers .= 'Reply-To: '.$field_email."\r\n";
$error_message = "";
$string_exp1 = "/^[A-Za-z ]+$/";
$string_exp2 = "/^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$/";
$string_exp3 = "/^[0-9]/";
$string_name = "/Your Name.../";
$string_phone = "/Phone Number.../";
$string_email = "/Email.../";
$string_message = "/Message.../";
$error_message .= 'From: '.$field_name."\n";
$error_message .= 'E-mail: '.$field_email."\n";
$error_message .= 'Phone: '.$field_phone."\n";
$error_message .= 'Message: '.$field_message."\n";
if(preg_match($string_name,trim($field_name))){
$error_message .= 'Please enter your name.<br />';
}
elseif(!preg_match($string_exp1,trim($field_name))){
$error_message .= 'The Name you entered does not appear to be valid.<br />';
}
if(preg_match($string_email,trim($field_email))){
$error_message .= 'Please enter your email.<br />';
}
elseif(!preg_match($string_exp2,trim($field_email))) {
$error_message .= 'The Email Address you entered does not appear to be valid.<br />';
}
if(preg_match($string_phone,trim($field_phone))){
$error_message .= 'Please enter your phone number.<br />';
}
elseif((!preg_match($string_exp3,trim($field_phone)))||(strlen(trim($field_phone))!=10)){
$error_message .= 'The phone number you entered does not appear to be valid.<br />';
}
if(preg_match($string_message,trim($field_message))){
$error_message .= 'Please enter your message.<br />';
}
elseif(strlen(trim($field_message)) < 4) {
$error_message .= 'The Message you entered does not appear to be valid.<br />';
}
if(strlen($error_message) > 0){
echo $error_message;
echo "<script>alert('Please correct the errors and try again!')</script>";
echo "<script>window.location = 'enquiry.html'</script>";
die();
}
$mail_status = mail($mail_to, $subject, $body_message, $headers);
if ($mail_status) { ?>
	<script language="javascript" type="text/javascript">
		alert('Thank you for the message. We will contact you shortly.');
		window.location = 'enquiry.html';
	</script>
<?php
}
else { ?>
	<script language="javascript" type="text/javascript">
		alert('Message failed. Please, send an email to nextdoor.overseas@gmail.com');
		window.location = 'enquiry.html';
	</script>
<?php
}
?>
