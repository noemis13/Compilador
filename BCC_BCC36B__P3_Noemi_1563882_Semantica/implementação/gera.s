	.text
	.file	"gera.ll"
	.globl	main                    # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# BB#0:                                 # %entry
	subq	$24, %rsp
.Lcfi0:
	.cfi_def_cfa_offset 32
	callq	leiaFlutuante
	cvttss2si	%xmm0, %eax
	movl	%eax, 12(%rsp)
	callq	leiaFlutuante
	cvttss2si	%xmm0, %eax
	movl	%eax, 16(%rsp)
	cvtsi2ssl	12(%rsp), %xmm0
	callq	escrevaFlutuante
	movl	12(%rsp), %eax
	addl	%eax, %eax
	addq	$24, %rsp
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function

	.section	".note.GNU-stack","",@progbits
