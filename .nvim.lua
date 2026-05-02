vim.schedule(function()
	local deb = require("utils.debounce"):new(1000)

	local ovs = require("overseer")

	local parse_gen_task = ovs.new_task({
		cmd = "antlr4",
		args = { "*.g4", "-visitor", "-o", "../" },
		cwd = "./lmat-cas-client/lmat_cas_client/compiling/antlr/grammar/",
		name = "Antlr4 Parser Generate",
	})

	local parse_tree_task = ovs.new_task({
		cmd = '"../../../../.venv/Scripts/python"',
		args = { "debug.py" },
		cwd = "./lmat-cas-client/lmat_cas_client/compiling/antlr/",
		name = "Antlr4 Parse Tree Generate",
	})

	parse_gen_task:subscribe("on_complete", function(_, status, _)
		if status == "SUCCESS" then
			parse_tree_task:restart()
		end
	end)

	vim.api.nvim_create_autocmd("BufWritePost", {
		pattern = "*.g4",
		callback = deb:debounced(function(_)
			parse_gen_task:restart()
		end),
	})

	local deb2 = require("utils.debounce"):new(1000)

	vim.api.nvim_create_autocmd("BufWritePost", {
		pattern = "*in.txt",
		callback = deb2:debounced(function(_)
			parse_tree_task:restart()
		end),
	})
end)
