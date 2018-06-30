	.text
	.file	"programa.ll"
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
	xorps	%xmm0, %xmm0
	cvtsi2ssl	12(%rsp), %xmm0
	cvtsi2ssl	16(%rsp), %xmm1
	addss	%xmm0, %xmm1
	cvttss2si	%xmm1, %eax
	addq	$24, %rsp
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function

	.section	".note.GNU-stack","",@progbits
