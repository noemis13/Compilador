	.text
	.file	"gera.ll"
	.globl	main                    # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# BB#0:                                 # %entry
	pushq	%rax
.Lcfi0:
	.cfi_def_cfa_offset 16
	movl	$10, n(%rip)
	movl	$0, soma(%rip)
	xorl	%eax, %eax
	.p2align	4, 0x90
.LBB0_1:                                # %repita
                                        # =>This Inner Loop Header: Depth=1
	movl	n(%rip), %ecx
	movl	%ecx, soma(%rip)
	movl	$1, n(%rip)
	testb	%al, %al
	jne	.LBB0_1
# BB#2:                                 # %fim
	movl	n(%rip), %eax
	cvtsi2ssl	%eax, %xmm0
	callq	escrevaFlutuante
	xorl	%eax, %eax
	popq	%rcx
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	n,@object               # @n
	.comm	n,4,4
	.type	soma,@object            # @soma
	.comm	soma,4,4
	.type	a,@object               # @a
	.comm	a,4,4
	.type	b,@object               # @b
	.comm	b,4,4

	.section	".note.GNU-stack","",@progbits
