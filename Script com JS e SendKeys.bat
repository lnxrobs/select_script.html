echo off
SET SendKeys=CScript //nologo //
E:JScript "%~F0" 

TIMEOUT /t 3 
%SendKeys% "null"
%SendKeys% "{null}"
%SendKeys% "null"
%SendKeys% "null"
%SendKeys% "{null}"

GOTO :EOF 

@end 
// JScript section 
var WshShell = 
Escript.CreateObject("WScript.Shell");
WshShell.SendKeys(WScript.Arguments
(0));0
